import sqlalchemy
from sqlalchemy import create_engine, orm
from psycopg2 import OperationalError

DEBUG = False
DEBUG_URL = "postgres://example:example@0.0.0.0:5432"
DEBUG_DB = "test"
DEBUG_FULL_PATH_DB = "{}/{}".format(DEBUG_URL, DEBUG_DB)

class DBSessionFactory(object):
	def __init__(self, connection_string):
		self._con_string = connection_string

	def _create_conn(self):
		print("Creating DB connection")
		self._engine = create_engine(self._con_string, echo=DEBUG)
		self._connection = self._engine.connect()

	@classmethod
	def setup(cls, connection_string, tables):
		if connection_string is None:
			cls._create_dev_db()
			connection_string = DEBUG_FULL_PATH_DB
		factory = cls(connection_string)
		factory._create_conn()
		session_class = orm.sessionmaker(bind=factory._engine)
		factory._session = orm.scoped_session(session_class)
		factory._create_tables(tables)
		return factory

	@classmethod
	def _create_dev_db(self):
		try:
			# verify that db exists
			e = create_engine(DEBUG_FULL_PATH_DB)
			connection = e.connect()
		except OperationalError:
			# db doesnt exists. create it
			e = create_engine(DEBUG_URL)
			connection = e.connect()
			connection.execute("commit")
			connection.execute("create database %s" % DEBUG_DB)
		connection.close()

			

	def _create_tables(self, tables):
		tables.metadata.create_all(self.engine)

	def get_session(self):
		return DBSession(self._session)

	@property
	def engine(self):
		return self._engine

class DBSession(object):
	def __init__(self, session):
		print("setting db session")
		self._session = session

	@property
	def db(self):
		return self._session
	
