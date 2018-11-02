import pytest
import os

from divorce_life.data_models.db import DBSessionFactory
from divorce_life.data_models.models import	Base

DATABASE_URL = os.environ.get('DATABASE_URL')

@pytest.fixture(scope="module")
def db_factory(request):
	db_factory = DBSessionFactory.setup(DATABASE_URL, Base)
	yield db_factory
	db_factory.close()

