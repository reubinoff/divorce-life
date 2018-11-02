
from .. import app
from flask import jsonify

HTTP_BAD_REQUEST = 400
HTTP_FORBIDDEN = 403
HTTP_NOT_FOUND = 404
HTTP_METHOD_NOT_ALLOWED = 405


class RequestInvalid(Exception):
	status_code = HTTP_BAD_REQUEST
	def __init__(self, message="Invalid Request.", status_code=None, payload=None):
		Exception.__init__(self)
		self.message = message
		if status_code is not None:
			self.status_code = status_code
		self.payload = payload

class ResourceNotFound(RequestInvalid):
	def __init__(self, message="Resource not found."):
		super(ResourceNotFound, self).__init__(message, HTTP_NOT_FOUND)


# register error handler
@app.errorhandler(RequestInvalid)
def handle_invalid_request(error):
	response = jsonify(error.message)
	response.status_code = error.status_code
	return response

