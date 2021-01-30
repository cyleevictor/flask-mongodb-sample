from flask import Flask, json, request

import data.conn as conn
import itemService
import orderService
from data.orders import Order
from data.items import Item

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
    req_data = request.get_json()

    order = Order(
        order_id=req_data['order_id'],
        table_id=req_data['table_id'],
        ordered_items=req_data['ordered_items'],
        description=req_data['description']
    )
    return orderService.add_order(order)


@app.route("/deleteOrder/<order_id>")
def delete_order(order_id):
    return orderService.delete_order(order_id)


# End point for Item

@app.route("/listItems")
def list_items():
    item_list = itemService.list_items_json()
    return item_list


@app.route("/listItem/<item_id>")
def list_item_by_id(item_id):
    item_list = itemService.list_item_json(item_id)
    return item_list


# Another way to list item
@app.route("/listItemLite")
def list_items_v2():
    item_list = itemService.list_items()
    json_string = json.dumps([item.json() for item in item_list])

    response = app.response_class(
        response=json_string,
        status=200,
        mimetype='application/json'
    )
    return response


@app.route("/addItems", methods=["POST"])
def add_items():
    req_data = request.get_json()

    item = Item(
        item_id=req_data['item_id'],
        name=req_data['name'],
        type=req_data['type'],
        price=req_data['price']
    )
    return itemService.add_item(item)


@app.route("/deleteItem/<item_id>")
def delete_item(item_id):
    return itemService.delete_item(item_id)


if __name__ == "__main__":
    conn.init()

    print("Start Flask...")
    app.run(host=HOST_NAME, port=PORT)
    print("Flask started.")
