from flask import Flask, jsonify
from flask_restful import Resource, marshal_with


from .. import  api

from .data_structures import ExpenseSchema
from .errors import ResourceNotFound
from .helpers import expect_json_data, ok_response
from .handlers import handlers


class ExpensesRoute(Resource):
	def get(self):
		"""
		Get expenses list
		"""
		expenses = handlers.expense.get_expenses()
		schema = ExpenseSchema(many=True)
		return schema.dump(expenses)

	@expect_json_data
	def post(self, data):
		"""
		create new expense item
		"""

		schema = ExpenseSchema()
		expense = handlers.expense.add_expense(data.get("name"), data.get("date_reported"), data.get("date_expense"))
		return schema.dump(expense)


class ExpenseRoute(Resource):
	def get(self, expense_id):
		"""
		Get expense by id
		"""
		try:
			expense = handlers.expense.get_expense_by_id(expense_id=expense_id)
			schema = ExpenseSchema()
			return schema.dump(expense)
		except KeyError:
			raise ResourceNotFound()


	@expect_json_data
	def post(self, data, expense_id):
		"""
		update spesific expense by ID
		"""
		try:
			expense = handlers.expense.update_expense(expense_id=expense_id, **data)
			schema = ExpenseSchema()
			return schema.dump(expense)
		except KeyError:
			raise ResourceNotFound()

	def delete(self, expense_id):
		"""
		delete expense item by id
		"""
		try:
			handlers.expense.delete_expense_by_id(expense_id=expense_id)
		except KeyError:
			raise ResourceNotFound()
		return ok_response()

api.add_resource(ExpensesRoute, '/expenses')
api.add_resource(ExpenseRoute, '/expense/<string:expense_id>')

