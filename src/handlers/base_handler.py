from ..data_models.db import DBSession, DBSessionFactory



class BaseHandler(object):
	def __init__(self, db_factory : DBSessionFactory):
		self._db_session = db_factory.get_session()
