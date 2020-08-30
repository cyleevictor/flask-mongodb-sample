import unittest

from main import app
from data import conn


class OrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        conn.init()

    def test_hello_world(self):
        tester = app.test_client(self)
        response = tester.get("/", content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello World!!')

    def test_list_order(self):
        tester = app.test_client(self)
        response = tester.get("/listOrders", content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_list_order_by_id(self):
        tester = app.test_client(self)
        order_id = "006"
        response = tester.get(f"/listOrder/{order_id}", content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_add_order(self):
        tester = app.test_client(self)
        content = {
            'order_id': '006',
            'table_id': 'Table9',
            'description': 'Chocolate2'
        }
        response = tester.post("/addOrders",
                               data=content
                               )
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_delete_order(self):
        tester = app.test_client(self)
        order_id = '006'
        response = tester.get(f"/deleteOrder/{order_id}", content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
