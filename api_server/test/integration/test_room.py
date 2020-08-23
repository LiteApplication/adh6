import json
import logging
import pytest

from src.interface_adapter.sql.model.database import Database as db
from config.TEST_CONFIGURATION import DATABASE as db_settings
from src.interface_adapter.sql.model.models import Chambre
from test.integration.resource import TEST_HEADERS, base_url


def assert_room_in_db(body):
    s = db.get_db().get_session()
    q = s.query(Chambre)
    q = q.filter(body["roomNumber"] == Chambre.numero)
    c = q.one()
    assert body["vlan"] == c.vlan.id
    assert body["description"] == c.description


def prep_db(session,
            sample_room1,
            sample_room2):
    session.add_all([
        sample_room1,
        sample_room2,
    ])
    session.commit()


@pytest.fixture
def api_client(sample_room1, sample_room2):
    from .context import app
    with app.app.test_client() as c:
        db.init_db(db_settings, testing=True)
        prep_db(db.get_db().get_session(),
                sample_room1, sample_room2)
        yield c


def test_room_filter_all_rooms(api_client):
    r = api_client.get(
        "{}/room/".format(base_url),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 2


def test_room_filter_all_rooms_limit_invalid(api_client):
    r = api_client.get(
        "{}/room/?limit={}".format(base_url, -1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_room_filter_all_rooms_limit(api_client):
    r = api_client.get(
        "{}/room/?limit={}".format(base_url, 1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 1


def test_room_filter_by_term(api_client, sample_room1):
    r = api_client.get(
        "{}/room/?terms={}".format(base_url, sample_room1.description),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 1


def test_room_get_valid_room(api_client, sample_room1):
    r = api_client.get(
        "{}/room/{}".format(base_url, sample_room1.id),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 4


def test_room_get_invalid_room(api_client):
    r = api_client.get(
        "{}/room/{}".format(base_url, 4900),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404


def test_room_post_new_room_invalid_vlan(api_client):
    room = {
        "roomNumber": 5111,
        "vlan": 45,
        "description": "Chambre 5111"
    }
    r = api_client.post(
        "{}/room/".format(base_url),
        data=json.dumps(room),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_room_post_new_room(api_client, sample_room1):
    room = {
        "roomNumber": 5111,
        "vlan": sample_room1.vlan.id,
        "description": "Chambre 5111",
    }
    r = api_client.post(
        "{}/room/".format(base_url),
        data=json.dumps(room),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201
    assert_room_in_db(room)


def test_room_put_update_room(api_client, sample_room1):
    room = {
        "vlan": sample_room1.vlan_id,
        "roomNumber": 5111,
        "description": "Chambre 5111"
    }
    r = api_client.put(
        "{}/room/{}".format(base_url, sample_room1.id),
        data=json.dumps(room),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 204
    assert_room_in_db(room)


def test_room_delete_existant_room(api_client, sample_room1):
    r = api_client.delete(
        "{}/room/{}".format(base_url, sample_room1.id),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 204

    s = db.get_db().get_session()
    q = s.query(Chambre)
    q = q.filter(Chambre.id == sample_room1.id)
    assert q.count() == 0


def test_room_delete_non_existant_room(api_client):
    r = api_client.delete(
        "{}/room/{}".format(base_url, 4900),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404
