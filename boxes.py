import requests
import json
import datetime

#url of firebase
url="https://inf551-fa849.firebaseio.com/"

#update pickup_Date
def update_pickup_date(password):
	myDate=datetime.date.today()
	dic={"pickup_date":{"year":myDate.year, "month":myDate.month, "day":myDate.day}}
	dic=json.dumps(dic)

	orders_in_control_panel=requests.get(url+"control_panel.json")
	orders_in_control_panel=orders_in_control_panel.json()
	box_in_database=requests.get(url+"express_box.json")
	box_in_database=box_in_database.json()
	for i in box_in_database:
		if box_in_database[i]['box_password']==password:
			box_id=i
	for i in orders_in_control_panel:
		if box_id==orders_in_control_panel[i]['box_id']:
			result = requests.patch(url + "control_panel/" + i + "/date.json", data=dic)
	return True


#judge password
def judge_password(password):
	password_in_database=[]
	result=requests.get(url+"express_box.json")
	result=result.json()
	for keys in result:
		password_in_database.append(result[keys]['box_password'])
	print (password_in_database)
	if password not in password_in_database:
		return False
	else:
		return True