from aiohttp import web
import inspect
import collections
import json

class BaseService(object):
	def __init__(self, backgroud_worker):
		self._worker = backgroud_worker


class BaseWorker(object):
	def __init__(self):
		self._server = None
		self._app = web.Application()
		self._service_functions = collections.defaultdict(list)
		self._services = dict()


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
			method = getattr(service, method_name)
		except AttributeError as e:
			raise e

		res = method(*args, **kwargs)

		return web.Response(text=res)

	def _prepare_route(self):
		self._app.add_routes([web.post('/{srv_name}/{srv_method}', self.handle)])


	def start(self):
		self._prepare_route()
		web.run_app(self._app)


class Test(BaseService):
	def __init__(self, backgroud_worker):
		super(Test, self).__init__(backgroud_worker)
	def srv_foo(self, *args, **kwargs):
		print("I am foo {}".format(kwargs))


class Worker(BaseWorker):
	def __init__(self):
		super(Worker, self).__init__()
		self.add_service('my_srv', Test(self))
	
	def run(self):
		self.start()

	


if __name__ == "__main__":
	worker = Worker()
	worker.run()

