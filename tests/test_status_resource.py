import pytest
import base64


def test_health_get(falcon_client):
    response = falcon_client.simulate_get("/status/health")

    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}


def test_dbconn_get(falcon_client):
    response = falcon_client.simulate_get("/status/db")

    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}


@pytest.mark.parametrize('user,password,code', (
        ('admin', 'sec', 200),
        ('admin', 'ec', 401),
        ('dmin', 'sec', 401),
        ('dmin', 'ec', 401),
))
def test_env_get(falcon_client, user, password, code):
    b64 = base64.b64encode(f'{user}:{password}'.encode()).decode('ascii')
    headers = {
        'Authorization': f'Basic {b64}'
    }
    response = falcon_client.simulate_get("/status/env", headers=headers)

    assert response.status_code == code


def test_env_get_no_auth(falcon_client):
    response = falcon_client.simulate_get("/status/env")

    assert response.status_code == 401


def test_env_get_bad_auth(falcon_client):
    response = falcon_client.simulate_get("/status/env", headers={'Authorization': 'Basic fdsfs'})

    assert response.status_code == 401
