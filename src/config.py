import os
import json


class Config(object):
	def __init__(self, config_file):
		self._config_file = config_file

	def init_config(self):
		if os.path.exists(self._config_file) is False:
			print("config file not found")
			return False
		if os.path.isfile(self._config_file) is False:
			print("invalid file")
			return False
		with open(self._config_file) as f:
			self._config_data = json.load(f)

	def get(self ,key, default_value=None):
		return self._config_data.get(key, default_value)

	def set(self, key, value):
		if key is None:
			raise KeyError
		self._config_data['key'] = value


