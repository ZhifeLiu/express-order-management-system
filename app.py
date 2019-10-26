from flask import Flask, render_template, request, flash
from control_panel import get_user_id,get_goods_id, get_cars_id, get_warehouses_id, \
    get_box_id,create_order,get_all_data,get_order_id
from boxes import update_pickup_date, judge_password
from warehouse import update_start_date, get_order_id_in_warehouse
from transports import get_order_id_in_transportation,update_arrive_date

app = Flask(__name__)
app.secret_key="ssss"

@app.route('/', methods=['POST', 'GET'])
def control_panel():
    if request.method=="GET":
        user_id=get_user_id()
        goods_id=get_goods_id()
        cars_id=get_cars_id()
        warehouse_id=get_warehouses_id()
        all_data=get_all_data()
        order_id=get_order_id()
        return render_template('control_panel.html', user_id=user_id, goods_id=goods_id,
                               cars_id=cars_id, warehouse_id=warehouse_id, all_data=all_data, order_id=order_id)
    if request.method=="POST":
        user = request.form["users"]
        good = request.form["goods"]
        car = request.form["cars"]
        warehouse = request.form["warehouses"]
        create_order(user,good,warehouse,car)
        user_id = get_user_id()
        goods_id = get_goods_id()
        cars_id = get_cars_id()
        warehouse_id = get_warehouses_id()
        all_data=get_all_data()
        order_id=get_order_id()
        return render_template('control_panel.html', user_id=user_id, goods_id=goods_id,
                               cars_id=cars_id, warehouse_id=warehouse_id,all_data=all_data,order_id=order_id)

@app.route('/warehouse',methods=['GET','POST'])
def warehouse():
    if request.method == "GET":
        order_id=get_order_id_in_warehouse()
        return render_template('warehouse.html',order_id=order_id)
    if request.method == "POST":
        order_id_1=request.form["orders"]
        update_start_date(order_id_1)
        order_id=get_order_id_in_warehouse()
        return render_template('warehouse.html',order_id=order_id)



@app.route('/transportation',methods=['GET','POST'])
def transportation():
    if request.method == "GET":
        order_id = get_order_id_in_transportation()
        box_id=get_box_id()
        return render_template('car.html', order_id=order_id,box_id=box_id)
    if request.method == "POST":
        order_id_1 = request.form["order"]
        box_id_1=request.form["box"]
        update_arrive_date(order_id_1,box_id_1)
        order_id = get_order_id_in_transportation()
        box_id=get_box_id()
        return render_template('car.html', order_id=order_id,box_id=box_id)


@app.route('/box',methods=['GET','POST'])
def box():
    if request.method=="GET":
        return render_template('box.html')

    if request.method=='POST':
        password=request.form["password"]
        print(password)
        if judge_password(password):
            update_pickup_date(password)
            flash("Pick Up Successfully")
        else:
            flash("Wrong Password")
        return render_template('box.html')


if __name__ == '__main__':
    app.run()


