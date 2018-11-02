
from flask import Flask, jsonify
from flask_restful import Resource, marshal_with


from .. import  api


class Home(Resource):
	def get(self):
		return "OK"
api.add_resource(Home, '/')

