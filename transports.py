import json
import requests
import datetime

#url of firebase
url="https://inf551-fa849.firebaseio.com/"

def get_order_id_in_transportation():
	order_id=[]
	result=requests.get(url+"transportation/5555/orders.json")
	result=result.json()
	for keys in result:
		order_id.append(result[keys])
	return order_id



#update Arrive_Date
def update_arrive_date(order_id,box_id):
    myDate = datetime.date.today()
    dic = {"arrive_date": {"year": myDate.year, "month": myDate.month, "day": myDate.day}}
    dic=json.dumps(dic)
    dic1 = box_id
    dic1=json.dumps(dic1)
    dic1 = json.dumps(box_id)
    orders_in_control_panel = requests.get(url + "control_panel.json")
    orders_in_control_panel = orders_in_control_panel.json()
    for keys in orders_in_control_panel:
        if order_id == keys:
            result = requests.patch(url + "control_panel/" + keys + "/date.json", data=dic)
            result = requests.put(url + "control_panel/" + keys + "/box_id.json", data=dic1)