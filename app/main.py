from flask import Flask, jsonify, json, request
import orderService
import data.conn as conn
from data.orders import Order

app = Flask(__name__)

HOST_NAME = "127.0.0.1"
PORT = "5000"


@app.route("/")
def hello_world():
    return "Hello World!!"


@app.route("/listOrders")
def list_orders():
    order_list = orderService.list_orders_json()
    return order_list


@app.route("/listOrder/<order_id>")
def list_order_by_id(order_id):
    order_list = orderService.list_order_json(order_id)
    return order_list


# Another way to list order
@app.route("/listOrderLite")
def list_orders_v2():
    order_list = orderService.list_orders()
    json_string = json.dumps([order.json() for order in order_list])

    response = app.response_class(
        response=json_string,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/addOrders", methods=["POST"])
def add_orders():
    req_data = request.form

    order = Order(
        order_id=req_data['order_id'],
        table_id=req_data['table_id'],
        description=req_data['description']
    )
    return orderService.add_order(order)


@app.route("/deleteOrder/<order_id>")
def delete_order(order_id):
    return orderService.delete_order(order_id)


if __name__ == "__main__":
    conn.init()

    print("Start Flask...")
    app.run(host=HOST_NAME, port=PORT)
    print("Flask started.")
