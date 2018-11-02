import os

from ..data_models.db import	DBSessionFactory
from ..data_models.models import	Base

from ..handlers.expenses import ExpenseHandler

DATABASE_URL = os.environ.get('DATABASE_URL')


class Handlers(object):
	def __init__(self):
		self._db_factory = DBSessionFactory.setup(DATABASE_URL, Base)
		self._setup()
	
	def _setup(self):
		self._expense = ExpenseHandler(self._db_factory)
	
	@property
	def expense(self):
		return self._expense

handlers = Handlers()


