import json
import pytest

from config.TEST_CONFIGURATION import DATABASE as db_settings
from src.interface_adapter.sql.model.database import Database as db
from src.interface_adapter.sql.model.models import Port
from test.integration.resource import base_url, TEST_HEADERS


def prep_db(session,
            sample_port1,
            sample_port2,
            sample_room1):
    session.add_all([
        sample_port1,
        sample_port2,
        sample_room1,
    ])
    session.commit()


@pytest.fixture
def api_client(sample_port1, sample_port2, sample_room1):
    from .context import app
    with app.app.test_client() as c:
        db.init_db(db_settings, testing=True)
        prep_db(db.get_db().get_session(),
                sample_port1,
                sample_port2,
                sample_room1)
        yield c


def assert_port_in_db(body):
    s = db.get_db().get_session()
    q = s.query(Port)
    q = q.filter(Port.numero == body["portNumber"])
    p = q.one()
    assert body["portNumber"] == p.numero
    assert body["room"] == p.chambre.id
    assert body["switchObj"] == p.switch.id


def test_port_get_filter_all(api_client):
    r = api_client.get(
        "{}/port/".format(base_url),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert switches
    assert len(switches) == 2


def test_port_get_filter_all_with_invalid_limit(api_client):
    r = api_client.get(
        "{}/port/?limit={}".format(base_url, -1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_port_get_filter_all_with_limit(api_client):
    r = api_client.get(
        "{}/port/?limit={}".format(base_url, 1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert switches
    assert len(switches) == 1


def test_port_get_filter_by_switchid(api_client, sample_switch2):
    r = api_client.get(
        "{}/port/?filter[switchObj]={}".format(base_url, sample_switch2.id),
        headers=TEST_HEADERS
    )
    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert switches
    assert len(switches) == 1


def test_port_get_filter_by_room_with_results(api_client, sample_port1):
    r = api_client.get(
        "{}/port/?filter[room]={}".format(base_url, sample_port1.chambre.id),
        headers=TEST_HEADERS,
    )

    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert switches
    assert len(switches) == 2


def test_port_get_filter_by_room_without_result(api_client):
    r = api_client.get(
        "{}/port/?filter[room]={}".format(base_url, 4242),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert not switches
    assert len(switches) == 0


def test_port_get_filter_by_term_oid(api_client):
    r = api_client.get(
        "{}/port/?terms={}".format(base_url, "1.2"),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert switches
    assert len(switches) == 1


def test_port_get_filter_by_term_numero(api_client):
    r = api_client.get(
        "{}/port/?terms={}".format(base_url, "0/0/1"),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    switches = json.loads(r.data.decode())
    assert switches
    assert len(switches) == 1


def test_port_post_create_port_invalid_switch(api_client, sample_switch1, sample_room1):
    body = {
        "room": sample_room1.id,
        "switchObj": 4242,
        "portNumber": "1/0/4",
        "oid": "10104"
    }

    r = api_client.post(
        "{}/port/".format(base_url),
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_port_post_create_port_invalid_room(api_client, sample_switch1, sample_room1):
    body = {
        "room": 4242,
        "switchObj": sample_switch1.id,
        "portNumber": "1/0/4",
        "oid": "10104"
    }

    r = api_client.post(
        "{}/port/".format(base_url),
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_port_post_create_port(api_client, sample_switch1, sample_room1):
    body = {
        "room": sample_room1.id,
        "switchObj": sample_switch1.id,
        "portNumber": "1/0/4",
        "oid": "10104"
    }

    r = api_client.post(
        "{}/port/".format(base_url),
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201


def test_port_get_existant_port(api_client, sample_switch1, sample_port1):
    r = api_client.get(
        "{}/port/{}".format(base_url, sample_port1.id),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    switch = json.loads(r.data.decode())
    assert switch


def test_port_get_non_existant_port(api_client, sample_switch1, sample_port1):
    r = api_client.get(
        "{}/port/{}".format(base_url, 4242),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404


def test_port_put_update_port_invalid_switch(api_client,
                                             sample_port1):
    portNumber = "1/2/3"
    body = {
        "room": 5110,
        "switchObj": 999,
        "oid": "10101",
        "portNumber": portNumber
    }

    r = api_client.put(
        "{}/port/{}".format(base_url, sample_port1.id),
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404


def test_port_put_update_port(api_client, sample_switch1, sample_port1):
    portNumber = "1/2/3"
    body = {
        "room": sample_port1.chambre.id,
        "oid": "10101",
        "switchObj": sample_switch1.id,
        "portNumber": portNumber
    }

    assert sample_port1.numero != portNumber
    r = api_client.put(
        "{}/port/{}".format(base_url, sample_port1.id),
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 204
    assert sample_port1.numero == portNumber
    assert_port_in_db(body)


def test_port_put_update_non_existant_port(api_client,
                                           sample_switch1):
    portNumber = "1/2/3"
    body = {
        "room": 5110,
        "oid": "10101",
        "switchObj": sample_switch1.id,
        "portNumber": portNumber
    }

    r = api_client.put(
        "{}/port/{}".format(base_url, 4242),
        data=json.dumps(body),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404


def test_port_delete_port(api_client, sample_switch1, sample_port1):
    r = api_client.delete(
        "{}/port/{}".format(base_url, sample_port1.id),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 204

    s = db.get_db().get_session()
    q = s.query(Port)
    q = q.filter(Port.id == sample_port1.id)
    assert not s.query(q.exists()).scalar()


def test_port_delete_non_existant_port(api_client,
                                       sample_switch1):
    r = api_client.delete(
        "{}/port/{}".format(base_url, 4242),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404
