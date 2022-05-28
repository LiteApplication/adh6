import json
import pytest

from src.interface_adapter.sql.model.models import  db
from src.interface_adapter.sql.model.models import Chambre
from test.integration.resource import TEST_HEADERS, base_url


@pytest.fixture
def client(sample_room1,
            sample_room2):
    from .context import app
    from .conftest import prep_db, close_db
    if app.app is None:
        return
    with app.app.test_client() as c:
        prep_db(
            sample_room1,
            sample_room2
        )
        yield c
        close_db()


def assert_room_in_db(body):
    s = db.session()
    q = s.query(Chambre)
    q = q.filter(body["roomNumber"] == Chambre.numero)
    c = q.one()
    assert body["vlan"] == c.vlan.numero
    assert body["description"] == c.description


def test_room_filter_all_rooms(client):
    r = client.get(
        "{}/room/".format(base_url),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 2


@pytest.mark.parametrize(
    'sample_only', 
    [
        ("id"),
        ("roomNumber"),
        ("vlan"),
        ("description"),
    ])
def test_room_search_with_only(client, sample_only: str):
    r = client.get(
        f'{base_url}/room/?only={sample_only}',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200

    response = json.loads(r.data.decode('utf-8'))
    assert len(response) == 2
    assert len(set(sample_only.split(",") + ["__typename", "id"])) == len(set(response[0].keys()))


def test_room_search_with_unknown_only(client):
    sample_only = "azerty"
    r = client.get(
        f'{base_url}/room/?only={sample_only}',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_member_filter_all_with_invalid_limit(client):
    r = client.get(
        '{}/member/?limit={}'.format(base_url, -1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_member_filter_all_with_limit(client):
    r = client.get(
        '{}/member/?limit={}'.format(base_url, 1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200

    response = json.loads(r.data.decode('utf-8'))
    assert len(response) == 1


def test_room_filter_all_rooms_limit_invalid(client):
    r = client.get(
        "{}/room/?limit={}".format(base_url, -1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_room_filter_all_rooms_limit(client):
    r = client.get(
        "{}/room/?limit={}".format(base_url, 1),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 1


def test_room_filter_by_term(client, sample_room1):
    r = client.get(
        "{}/room/?terms={}".format(base_url, sample_room1.description),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 1


def test_room_get_valid_room(client, sample_room1):
    r = client.get(
        "{}/room/{}".format(base_url, sample_room1.id),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode())
    assert len(response) == 5


def test_room_get_invalid_room(client):
    r = client.get(
        "{}/room/{}".format(base_url, 4900),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404


def test_room_post_new_room_invalid_vlan(client):
    room = {
        "roomNumber": 5111,
        "vlan": 45,
        "description": "Chambre 5111"
    }
    r = client.post(
        "{}/room/".format(base_url),
        data=json.dumps(room),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404


def test_room_post_new_room(client, sample_room1):
    room = {
        "roomNumber": 5111,
        "vlan": sample_room1.vlan.numero,
        "description": "Chambre 5111",
    }
    r = client.post(
        "{}/room/".format(base_url),
        data=json.dumps(room),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201
    assert_room_in_db(room)


def test_room_put_update_room(client, sample_room1):
    room = {
        "vlan": sample_room1.vlan.numero,
        "roomNumber": 5111,
        "description": "Chambre 5111"
    }
    r = client.put(
        "{}/room/{}".format(base_url, sample_room1.id),
        data=json.dumps(room),
        content_type='application/json',
        headers=TEST_HEADERS,
    )
    assert r.status_code == 204
    assert_room_in_db(room)


def test_room_delete_existant_room(client, sample_room1):
    r = client.delete(
        "{}/room/{}".format(base_url, sample_room1.id),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 204

    s = db.session()
    q = s.query(Chambre)
    q = q.filter(Chambre.id == sample_room1.id)
    assert q.count() == 0


def test_room_delete_non_existant_room(client):
    r = client.delete(
        "{}/room/{}".format(base_url, 4900),
        headers=TEST_HEADERS,
    )
    assert r.status_code == 404
