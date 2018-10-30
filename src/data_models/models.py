from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expense(Base):
	__tablename__ = 'expense'
	id = Column(Integer, primary_key=True)
	name =  Column(String(50))

	def as_dict(self):
		return {c.name: getattr(self, c.name) for c in self.__table__.columns}

