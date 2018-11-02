import pytest
import os

from src.data_models.db import DBSessionFactory
from src.handlers.expenses import ExpenseHandler
from src.data_models.models import	Base

DATABASE_URL = os.environ.get('DATABASE_URL')

def test_my_first_test():
	db_factory = DBSessionFactory.setup(DATABASE_URL, Base)
	handler = ExpenseHandler(db_factory)
	a = handler.add_expense("moshe")
	assert a is not None
	assert True
