from ..data_models import models as MODEL
from marshmallow import Schema, fields, post_load

class ExpenseSchema(Schema):
	id = fields.Integer()
	name = fields.String(required=True)

	@post_load
	def create_db_model(self, data):
		return MODEL.Expense(**data)

