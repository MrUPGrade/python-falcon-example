import pytest
from falcon import testing

from pft.bootstrap import create_falcon_app


@pytest.fixture(scope='session')
def falcon_api():
    return create_falcon_app()


@pytest.fixture
def falcon_client(falcon_api):
    return testing.TestClient(falcon_api)
