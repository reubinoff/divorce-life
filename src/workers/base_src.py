from aiohttp import web
import inspect
import collections
import json


DEFAULT_IP="localhost"
DEFAULT_PORT=8088

class BaseService(object):
	def __init__(self, backgroud_worker):
		self._worker = backgroud_worker


class BaseWorker(object):
	def __init__(self, config_data):
		self._server = None
		self._app = web.Application()
		self._service_functions = collections.defaultdict(list)
		self._services = dict()
		self._prepare_route()
		self._config = config_data


	@property
	def app(self):
		return self._app

	def add_service(self, srv_name, srv):
		if isinstance(srv, BaseService) is False:
			raise
		self._render_methods(srv, srv_name)

	def _render_methods(self, srv, srv_name):
		methods = [foo for foo in dir(srv) if foo.startswith("srv_")]

		for attr_name in methods:
			attr = getattr(srv, attr_name)
			self._service_functions[srv_name].append(attr_name)

		self._services[srv_name] = srv

	async def handle(self, request):
		name = request.match_info.get('srv_name', "Anonymous")
		method_name = request.match_info.get('srv_method', "None")
		args = []
		kwargs = {}
		try:
			json_data = await request.text()
			if len(json_data) > 0:
				try:
					kwargs = json.loads(json_data)
				except json.decoder.JSONDecodeError as e:
					raise e
		except:
			raise

		service = self._services.get(name)
		try:
			method = getattr(service, method_name, None)
			if method is None:
				return web.Response(text="method not found", status=404)
		except AttributeError as e:
			raise e

		try:
			res = method(*args, **kwargs)
		except TypeError as e:
			return web.Response(text="Invalid request. {}".format(e), status=403)

		data = {
			"data": res or None,
			"status": "OK"
		}
		return web.Response(text=json.dumps(data))

	def _prepare_route(self):
		self._app.add_routes([web.post('/{srv_name}/{srv_method}', self.handle)])


	def start(self):
		web.run_app(self._app, host=self._config.get("ip", DEFAULT_IP), port=self._config.get("port", DEFAULT_PORT))



