import flask
from functools import wraps

from .errors import RequestInvalid

def expect_json_data(route_method):
	@wraps(route_method)
	def decorated(self, *args, **kwargs):
		data = flask.request.get_json(force=True, silent=True)
		if data is None:
			raise RequestInvalid("Payload is expected to be json!")
		return route_method(self, data, *args, **kwargs)
	return decorated

def ok_response():
	return flask.jsonify(status=True)
