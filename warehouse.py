import json
import requests
import datetime

#url of firebase
url="https://inf551-fa849.firebaseio.com/"

#show goods in each warehouse
def show_in_warehouse():
    goods_in_warehouse=requests.get(url+"warehouse/Goods_ID.json")
    Goods=requests.get(url+"Goods.json")
    Goods=Goods.json()
    return Goods

def get_order_id_in_warehouse():
	order_id=[]
	result=requests.get(url+"warehouse/111222/orders.json")
	result=result.json()
	for keys in result:
		order_id.append(result[keys])
	return order_id

#update Start_Date
def update_start_date(order_id):
	myDate=datetime.date.today()
	dic={"start_date":{"year":myDate.year, "month":myDate.month, "day":myDate.day}}
	dic=json.dumps(dic)
	orders_in_control_panel=requests.get(url+"control_panel.json")
	orders_in_control_panel=orders_in_control_panel.json()
	for keys in orders_in_control_panel:
		if order_id==keys:
			result=requests.patch(url+"control_panel/"+keys+"/date.json",data=dic)
