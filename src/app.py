import os
from flask import Flask, jsonify
from flask import render_template

from .data_models.db import	DBSessionFactory
from .data_models.models import	Base

from .handlers.expenses import ExpenseHandler

DATABASE_URL = os.environ.get('DATABASE_URL')

app = Flask(__name__)
db_factory = DBSessionFactory.setup(DATABASE_URL, Base)

@app.route("/")
def hello():
	handler = ExpenseHandler(db_factory)
	handler.add_expense()
	return "OK"

@app.route("/e")
def hello_():
	handler = ExpenseHandler(db_factory)
	res = handler.get_expenses()
	return jsonify(data = [x.as_dict() for x in res])
