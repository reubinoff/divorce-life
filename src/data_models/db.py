import sqlalchemy
from sqlalchemy import create_engine, orm
import os

DATABASE_URL = os.environ['DATABASE_URL']
DEBUG = True

class DBSession(object):
	def __init__(self, conn_string, db_tables):
		self._con_string = conn_string
		self._create_conn()
		self.create_tables(db_tables)


	def _create_tables(self, tables):
		tables.metadata.create_all(self._factory.engine)

	def _create_conn(self):
		print("Creating DB connection to {}".format(self._con_string))
		self._engine = create_engine(self._con_string, echo=DEBUG)
		self._connection = self._engine.connect()
		session_class = orm.sessionmaker(bind=self._engine)
		self._session = orm.scoped_session(session_class)

	@property
	def engine(self):
		return self._engine

	@property
	def db(self):
		return self._session
	
