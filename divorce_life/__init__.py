
from flask import Flask, jsonify
import flask_restful

app = Flask(__name__)
original_flask_handle_exception = app.handle_exception
original_flask_handle_user_exception = app.handle_user_exception
api = flask_restful.Api(app)



# modifies flask handle exception default behavior, but is implemented badly.
# api = flask_restful.Api(app)
#
# # so we restore flask default error handling behavior
app.handle_exception = original_flask_handle_exception
app.handle_user_exception = original_flask_handle_user_exception
#
