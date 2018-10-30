from .base_handler import BaseHandler
from ..data_models.models import Expense

class ExpenseHandler(BaseHandler):
	def __init__(self, db_factory):
		super().__init__(db_factory)
	
	def get_expenses(self):
		expense_list = self._db_session.db.query(Expense).all()
		return expense_list

	def add_expense(self):
		expense = Expense(name="exp_mose")
		try:
			self._db_session.db.add(expense)
			self._db_session.db.commit()
		except:
			self._db_session.db.rollback()
