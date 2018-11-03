from .base_handler import BaseHandler
from ..data_models.models import Expense

class ExpenseHandler(BaseHandler):
	def __init__(self, db_factory):
		super().__init__(db_factory)
		self._db
	
	def get_expenses(self):
		expense_list = self._db.query(Expense).all()
		return expense_list

	def add_expense(self, name, date_reported, date_expense):
		expense = Expense(name=name, date_reported=date_reported, date_expense=date_expense)
		try:
			self._db.add(expense)
			self._db.commit()
		except:
			self._db.rollback()
		return expense

	def _get_expense(self, **filters):
		query = self._db.query(Expense)
		for attr,value in filters.items():
			query = query.filter(getattr(Expense,attr)==value)
		expense = query.first()
		if expense is None:
			raise KeyError('Not found')
		return expense

	def get_expense_by_name(self, expense_name):
		return self._get_expense(name=expense_name)


	def get_expense_by_id(self, expense_id):
		return self._get_expense(id=expense_id)


	def delete_expense_by_id(self, expense_id):
		expense = self._get_expense(id=expense_id)
		try:
			self._db.delete(expense)
			self._db.commit()
		except:
			self._db.rollback()
			raise

	def update_expense(self, expense_id, **kwargs):
		if len(kwargs) == 0:
			return

		expense = self._get_expense(id=expense_id)
		for key, value in kwargs.items():
			if "id" in key:
				continue
			if value is not None:
				setattr(expense, key, value)
		try:
			self._db.commit()
		except:
			self._db.rollback()
			raise
		return expense



