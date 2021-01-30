from mongoengine import Document, StringField, DecimalField


class Item(Document):
    item_id = StringField(required=True)
    name = StringField(required=True)
    type = StringField(required=True)
    price = DecimalField(required=True)

    def json(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'type': self.type,
            'price': self.price
        }

    meta = {
        'db_alias': 'core',
        'collection': 'items'
    }
