import time, datetime
from .setup_env import client
from divorce_life.routes.errors import ResourceNotFound


def test_get_list(client):
    """Start with a blank database."""

    rv = client.get('/expenses')
    assert rv.data is not None

def test_add_expense(client):
	body = {
		"name": "test",
		"date_reported": datetime.datetime.now(),
		"date_expense": datetime.datetime.now()
	}
	rv = client.post('/expenses', json=body)
	assert "id" in rv.json
	assert rv.json["id"] is not None
	new_rv = client.get('/expense/'+str(rv.json["id"]))
	assert new_rv.json["id"] is not None


def test_delete_expense(client):
	body = {
		"name": "test",
		"date_reported": datetime.datetime.now(),
		"date_expense": datetime.datetime.now()
	}
	rv_list_1 = client.get('/expenses').json
	rv = client.post('/expenses', json=body)
	assert "id" in rv.json
	id = str(rv.json["id"])
	assert id is not None
	rv_list_2 = client.get('/expenses').json
	assert len(rv_list_1)+1 == len(rv_list_2)
	del_st = client.delete('/expense/'+id)
	assert del_st.status_code == 200
	rv_list_3 = client.get('/expenses').json
	assert len(rv_list_1) == len(rv_list_3)
	# try:
	# 	del_st = client.delete('/expense/'+id)
	# except ResourceNotFound:
	# 	return
	# assert False


def test_update_expense(client):
	body = {
		"name": "test",
		"date_reported": datetime.datetime.now(),
		"date_expense": datetime.datetime.now()
	}
	rv = client.post('/expenses', json=body)
	assert "id" in rv.json
	assert rv.json["id"] is not None
	new_rv = client.get('/expense/'+str(rv.json["id"]))
	assert new_rv.json["id"] is not None
	update_rv = client.post('/expense/'+str(rv.json["id"]), json={"name": "new"})
	new_rv = client.get('/expense/'+str(rv.json["id"]))
	assert new_rv.json["name"] == "new"
	


