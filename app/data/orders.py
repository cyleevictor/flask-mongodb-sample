import mongoengine
from mongoengine import Document, EmbeddedDocument, StringField, IntField, DecimalField, ListField, EmbeddedDocumentField


class OrderedItem(EmbeddedDocument):
    # id = ObjectIdField()
    item_id = StringField(required=True)
    quantity = IntField(required=True)
    sub_total = DecimalField(required=True)

    def json(self):
        return {
            # 'id': self.id,
            'item_id': self.item_id,
            'quantity': self.quantity,
            'sub_total': self.sub_total
        }

class Order(Document):
    order_id = StringField(required=True)
    table_id = StringField(required=True)
    ordered_items = ListField(EmbeddedDocumentField(OrderedItem))
    description = StringField(required=False)

    def json(self):
        return {
            'order_id': self.order_id,
            'table_id': self.table_id,
            'ordered_items': self.ordered_items,
            'description': self.description
        }

    meta = {
        'db_alias': 'core',
        'collection': 'orders'
    }

