import unittest

from main import app
from data import conn


class ItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        conn.init()

    def test_list_item(self):
        tester = app.test_client(self)
        response = tester.get("/listItems", content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_list_item_by_id(self):
        tester = app.test_client(self)
        item_id = "I001"
        response = tester.get(f"/listItem/{item_id}", content_type='html/text')
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_add_item(self):
        tester = app.test_client(self)
        content = {
            'item_id': 'I001',
            'name': 'Lemon Tea',
            'type': 'Beverages',
            'price': 10
        }

        response = tester.post("/addItems",
                               json=content
                               )
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        print(response.data)

    def test_delete_item(self):
        tester = app.test_client(self)
        item_id = 'I001'
        response = tester.get(f"/deleteItem/{item_id}", content_type='html/text')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
