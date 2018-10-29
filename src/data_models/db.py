import sqlalchemy
from sqlalchemy import create_engine, orm
import os

DATABASE_URL = os.environ['DATABASE_URL']
DEBUG = True

class DBSession(object):
	def __init__(self, session, factory):
		self._session = session
		self._factory = factory


	def create_tables(self, tables):
		tables.metadata.create_all(self._factory.engine)


class DBFactory(object):
	def __init__(self, conn_string):
		self._con_string = conn_string

	def _create_conn(self):
		self._engine = create_engine(self._con_string, echo=DEBUG)
		self._connection = self._engine.connect()
		session_class = orm.sessionmaker(bind=self._engine)
		session = orm.scoped_session(session_class)
		return DBSession(session)

	@property
	def engine(self):
		return self._engine

	@classmethod
	def setup_db(cls, connection_string, db_tables)
		session = cls(connection_string)

		session.create_tables(db_tables)

