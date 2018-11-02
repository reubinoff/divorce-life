import pytest
import os

from .setting_env import db_factory
from src.handlers.expenses import ExpenseHandler


def test_my_first_test(db_factory):
	handler = ExpenseHandler(db_factory)
	a = handler.add_expense("moshe")
	assert a is not None
	assert True
