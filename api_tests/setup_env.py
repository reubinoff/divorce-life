import pytest

from divorce_life.app import app

@pytest.fixture
def client():
	with app.test_client() as c:
		yield c

