import json
from typing import List

from data.items import Item


def add_item(item: Item):
    try:
        item.save()
        print(f"Added item {item.item_id}")
        return f"Added item: {item.json()}"
    except Exception as e:
        print("Error adding item", e)
        return None


def list_items() -> List[Item]:
    query = Item.objects()
    items = list(query)
    return items


def list_items_json():
    query = Item.objects()

    json_string = query.to_json()
    dicts = json.loads(json_string)
    print(dicts)
    return json_string


def list_item_json(item_id):
    query = Item.objects(item_id=item_id)
    json_string = query.to_json()
    return json_string


def delete_item(item_id):
    query = Item.objects(item_id=item_id)
    json_string = query.to_json()
    cnt = query.count()
    print(f"Count: {cnt}")
    query.delete()

    return json_string