from base_src import BaseService, BaseWorker



class ExpenseService(BaseService):
	def __init__(self, backgroud_worker):
		super(ExpenseService, self).__init__(backgroud_worker)
	
	def get_list(self):
		return self._worker.get_list()


class ExpenseWorker(BaseWorker):
	def __init__(self):
		super(ExpenseWorker, self).__init__()
		self.add_service('expense_service', ExpenseService(self))
	def get_list(self):
		return {
			"asdasd": 3,
			"safsadf": [2,4,5,67,4,3,3],
			"dsgegrerg": True
		}



if __name__ == "__main__":
	worker = ExpenseWorker()
	worker.start()


