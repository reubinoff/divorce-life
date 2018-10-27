import sys
import argparse
import importlib
from config import Config





def init_workers(workers_data: dict):
	"""
	init workers from config file and return the success workers name
	"""
	if workers_data is None:
		return []
	workers_name = []
	workers = dict()
	for worker_name, worker_data in workers_data.items():
		print(worker_name)
		module_name, class_name = worker_data.get("app", "").rsplit(".", 1)
		module = importlib.import_module(module_name)
		class_obj = getattr(module, class_name)
		class_instance = class_obj(worker_data)
		workers[worker_name] = class_instance
		workers_name.append(worker_name)
		class_instance.start()

	return workers_name



if __name__ == "__main__":
	print('Starting....')
	parser = argparse.ArgumentParser(description='Just Application')
	parser.add_argument('-c', '--config', help='config file', required=True)
	args = parser.parse_args()


	app_config = Config(args.config)
	config_loaded = app_config.init_config()
	if config_loaded is False:
		sys.exit(1)
	workers_name_list = init_workers(app_config.get("workers"))
	if len(workers_name_list) == 0:
		print("No worker started")
		sys.exit(1)


