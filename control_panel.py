import requests
import json
import datetime
import uuid

#url of firebase
url="https://inf551-fa849.firebaseio.com/"

#get all data from database
def get_all_data():
    result=requests.get(url+".json")
    result=result.json()
    return result

#get users' id from database
def get_user_id():
    user_id=[]
    result=requests.get(url+"user.json")
    result=result.json()
    for keys in result:
        user_id.append(keys)
    return user_id

#get goods' id from database
def get_goods_id():
    goods_id=[]
    result=requests.get(url+"goods.json")
    result=result.json()
    for keys in result:
        goods_id.append(keys)
    return goods_id

#get cars' id from database
def get_cars_id():
    cars_id=[]
    result=requests.get(url+"transportation.json")
    result=result.json()
    for keys in result:
        cars_id.append(keys)
    return cars_id

#get warehouses' id from database
def get_warehouses_id():
    warehouses_id=[]
    result=requests.get(url+"warehouse.json")
    result=result.json()
    for keys in result:
        warehouses_id.append(keys)
    return warehouses_id

#get boxes' id from database
def get_box_id():
    box_id=[]
    result=requests.get(url+"express_box.json")
    result=result.json()
    for keys in result:
        box_id.append(keys)
    return box_id

def get_order_id():
    order_id=[]
    result=requests.get(url+"control_panel.json")
    result=result.json()
    if result:
        for keys in result:
            order_id.append(keys)
    return order_id

#Create a new order and upload it to the database
def create_order(user_id,goods_id,warehouse_id,car_id):
    myDate = datetime.date.today()
    dic={"user_id":user_id,"goods_id":goods_id, "warehouse_id":warehouse_id, "car_id":car_id,
         "date":{"order_date":{"year":myDate.year,"month":myDate.month,"day":myDate.day}}}
    dic=json.dumps(dic)
    order_id=uuid.uuid1()
    result=requests.put(url+"control_panel/"+str(order_id)+".json", data=dic)
    dic1=json.dumps(str(order_id))
    result=requests.post(url+"warehouse/"+warehouse_id+"/orders.json",data=dic1)
    result=requests.post(url+"transportation/"+car_id+"/orders.json",data=dic1)
    return "success"




