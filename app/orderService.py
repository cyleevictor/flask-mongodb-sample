import json
from typing import List

from data.orders import Order


def add_order(order: Order):
    try:
        order.save()
        print(f"Added order {order.order_id}")
        return f"Added order: {order.json()}"
    except Exception as e:
        print("Error adding order", e)
        return None


def list_orders() -> List[Order]:
    query = Order.objects()
    orders = list(query)
    return orders


def list_orders_json():
    query = Order.objects()

    json_string = query.to_json()
    dicts = json.loads(json_string)
    print(dicts)
    return json_string


def list_order_json(order_id):
    query = Order.objects(order_id=order_id)
    json_string = query.to_json()
    return json_string


def delete_order(order_id):
    query = Order.objects(order_id=order_id)
    json_string = query.to_json()
    cnt = query.count()
    print(f"Count: {cnt}")
    query.delete()

    return json_string