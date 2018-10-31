import os
from flask import Flask, jsonify
from flask import render_template
from flask_restful import Resource

from .data_models.db import	DBSessionFactory
from .data_models.models import	Base

from .handlers.expenses import ExpenseHandler

from . import app, api

DATABASE_URL = os.environ.get('DATABASE_URL')

db_factory = DBSessionFactory.setup(DATABASE_URL, Base)
handler = ExpenseHandler(db_factory)

class ExpensesRoute(Resource):
    def get(self):
		"""
		Get expenses list
		"""
        return {'hello': 'world'}

	def post(self):
		"""
		create new expense item
		"""
		return "OK"


class ExpenseRoute(Resource):
    def get(self, expense_id):
		"""
		Get expense by id
		"""
        return {'hello': 'world'}

	def post(self, expense_id):
		"""
		update spesific expense by ID
		"""
		return "OK"

	def delete(self, expense_id):
		"""
		delete expense item by id
		"""
		return "Deleted"

api.add_resource(ExpensesRoute, '/expenses')
api.add_resource(ExpenseRoute, '/expense/<string:expense_id>')


@app.route("/")
def hello():
	handler.add_expense()
	return "OK"

@app.route("/e")
def hello_():
	res = handler.get_expenses()
	return jsonify(data = [x.as_dict() for x in res])
