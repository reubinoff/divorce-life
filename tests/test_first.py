import pytest

from divorce_life.handlers.expenses import ExpenseHandler
from .setting_env import db_factory


def test_add_get_Expense(db_factory):
	handler = ExpenseHandler(db_factory)
	expense = handler.add_expense("moshe")
	assert expense is not None
	new_expense = handler.get_expense_by_id(expense.id)
	assert new_expense is not None

def test_update_get_Expense(db_factory):
	handler = ExpenseHandler(db_factory)
	expense = handler.add_expense("moshe")
	assert expense is not None
	expense = handler.update_expense(expense.id, name="moshe_2")
	new_expense = handler.get_expense_by_id(expense.id)
	assert new_expense is not None
	assert new_expense.name == "moshe_2"


def test_delete_get_Expense(db_factory):
	handler = ExpenseHandler(db_factory)
	expense = handler.add_expense("moshe")
	assert expense is not None
	new_expense = handler.get_expense_by_id(expense.id)
	assert new_expense is not None
	new_expense = handler.delete_expense_by_id(expense.id)
	try:
		new_expense = handler.get_expense_by_id(expense.id)
	except KeyError:
		return
	assert False

