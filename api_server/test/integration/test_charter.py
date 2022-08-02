import datetime
import json
import pytest
from sqlalchemy import select
from test import SAMPLE_CLIENT, SAMPLE_CLIENT_ID

from test.integration.resource import TEST_HEADERS, TEST_HEADERS_SAMPLE, base_url as host_url
from adh6.storage.sql.models import Adherent
from adh6.storage import db

base_url = f'{host_url}/charter/'

@pytest.fixture
def sample_member(faker):
    yield Adherent(
        id=SAMPLE_CLIENT_ID,
        nom='Dubois',
        prenom='Jean-Louis',
        mail='j.dubois@free.fr',
        login=SAMPLE_CLIENT,
        password='a',
        ip=faker.ipv4_public(),
        subnet=faker.ipv4('c'),
        mail_membership=249
    )


@pytest.fixture
def client(sample_member):
    from .context import app
    from .conftest import prep_db, close_db
    if app.app is None:
        return
    with app.app.test_client() as c:
        prep_db(sample_member)
        yield c
        close_db()


def test_charter_sign_minet(client, sample_member):
    r = client.post(
        f"{base_url}{1}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201
    assert db.session().execute(select(Adherent.datesignedminet).where(Adherent.id == sample_member.id)).scalar_one()


def test_charter_sign_hosting(client, sample_member):
    r = client.post(
        f"{base_url}{2}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201
    assert db.session().execute(select(Adherent.datesignedhosting).where(Adherent.id == sample_member.id)).scalar_one()


@pytest.mark.parametrize('charter', [1, 2])
def test_charter_sign_unknown_member(client, charter):
    r = client.post(
        f"{base_url}{charter}/member/{200}",
        headers=TEST_HEADERS
    )
    assert r.status_code == 404


@pytest.mark.parametrize('charter', [1, 2])
def test_charter_sign_unauthorized(client, sample_member, charter):
    r = client.post(
        f"{base_url}{charter}/member/{sample_member.id}",
        headers=TEST_HEADERS_SAMPLE,
    )
    assert r.status_code == 403


def test_charter_sign_bad_charter(client, sample_member):
    r = client.post(
        f"{base_url}{4}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


@pytest.mark.parametrize('charter,length', [(1, 0), (2, 1)])
def test_charter_list_members(client, sample_member, charter, length):
    r = client.post(
        f"{base_url}{2}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201

    r = client.get(
        f"{base_url}{charter}/member/",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode('utf-8'))
    assert len(response) == length


def test_charter_list_members_bad_charter(client):
    r = client.get(
        f"{base_url}{4}/member/",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 400


def test_charter_list_members_unauthorized(client):
    r = client.get(
        f"{base_url}{4}/member/",
        headers=TEST_HEADERS_SAMPLE,
    )
    assert r.status_code == 403


@pytest.mark.parametrize('charter', [1, 2])
def test_charter_get_not_signed(client, sample_member, charter):
    r = client.get(
        f"{base_url}{charter}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = r.text
    assert response == ''


@pytest.mark.parametrize('charter', [1, 2])
def test_charter_get_already_signed(client, sample_member, charter):
    r = client.post(
        f"{base_url}{charter}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 201

    r = client.get(
        f"{base_url}{charter}/member/{sample_member.id}",
        headers=TEST_HEADERS,
    )
    assert r.status_code == 200
    response = json.loads(r.data.decode('utf-8'))
    assert response != ''


@pytest.mark.parametrize('charter', [1, 2])
def test_charter_get_unknown_member(client, charter):
    r = client.get(
        f"{base_url}{charter}/member/{200}",
        headers=TEST_HEADERS
    )
    assert r.status_code == 404


@pytest.mark.parametrize('charter', [1, 2])
def test_charter_get_unauthorized(client, sample_member, charter):
    r = client.get(
        f"{base_url}{charter}/member/{sample_member.id}",
        headers=TEST_HEADERS_SAMPLE,
    )
    assert r.status_code == 403
