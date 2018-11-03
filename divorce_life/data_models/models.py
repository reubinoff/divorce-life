from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Expense(Base):
	__tablename__ = 'expense'
	id = Column(Integer, primary_key=True)
	name =  Column(String(50), nullable=False)
	date_reported = Column(Date(), nullable=False)
	date_expense = Column(Date(), nullable=False)

