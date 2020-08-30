import mongoengine


class Order(mongoengine.Document):
    order_id = mongoengine.StringField(required=True)
    table_id = mongoengine.StringField(required=True)
    description = mongoengine.StringField(required=False)

    def json(self):
        return {
            'order_id': self.order_id,
            'table_id': self.table_id,
            'description': self.description
        }

    meta = {
        'db_alias': 'core',
        'collection': 'orders'
    }

