import unittest
import random

from pymongo import MongoClient

from ..app import app


class TestWebservice(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = app.test_client()
        self.inserted_item = None
        self.mongo_client = MongoClient('mongodb', 27017)
        self.db = self.mongo_client['orders']
        self.items = self.db.items
        self.orders = self.db.orders
        self.item_keys = ['_id', 'description', 'price', 'quantity']
        self.order_keys = ['_id', 'items', 'total']

    def tearDown(self):
        if self.inserted_item is not None:
            self.test_delete_item()

    def test_retrieve_items(self):
        """Tests retrieving a list of items and getting the correct response"""
        response = self.client.get('items')
        self.assertEqual(response.status_code, 200)
        json = response.json
        for item in json['_items']:
            self.assertTrue(all([k in item for k in self.item_keys]))

    def test_get_item(self):
        """Tests getting an item and getting the correct response"""
        db_id = self.items.find_one()['_id']
        response = self.client.get('items/' + str(db_id))
        self.assertEqual(response.status_code, 200)
        json = response.json
        self.assertTrue(all([k in json for k in self.item_keys]))

    @unittest.skip('404 error handled by Eve framework')
    def test_get_not_found_item(self):
        """Tests getting an non-existing item and getting a 404"""
        pass

    def test_add_item(self):
        """Tests adding an item and getting the correct response"""
        description = 'test description'
        quantity = 4
        price = 23.50
        test_item = {
            'description': description,
            'quantity': quantity,
            'price': price
        }
        response = self.client.post('items', data=test_item)
        self.assertLess(response.status_code, 300)
        json = response.json
        self.assertIn('_id', json)
        item_id = json['_id']
        inserted_item = self.client.get('items/' + item_id).json
        self.assertTrue(inserted_item is not None)
        for k, v in test_item.items():
            self.assertIn(k, inserted_item)
            self.assertEqual(inserted_item[k], v)
        self.inserted_item = inserted_item

    @unittest.skip('400 error handled by Eve framework')
    def test_add_item_missing(self):
        """Tests trying to add an item with missing params and getting a 400"""
        pass

    def test_update_item(self):
        """Tests updating an item and getting the correct response"""
        new_description = 'new description'
        if self.inserted_item is None:
            self.test_add_item()
        item_id = self.inserted_item['_id']
        etag = self.inserted_item['_etag']
        headers = {'If-Match': etag}
        response = self.client.patch(
            'items/' + item_id, data={'description': new_description}, headers=headers)
        self.assertEqual(response.status_code, 200)
        json = response.json
        self.assertIn('_id', json)
        item_id = json['_id']
        inserted_item = self.client.get('items/' + item_id).json
        self.assertEqual(inserted_item['description'], new_description)
        self.inserted_item = inserted_item

    @unittest.skip('404 error handled by Eve framework')
    def test_update_ne_item(self):
        """Tests trying to update a non-existing item and getting a 404"""
        pass

    def test_delete_item(self):
        """Tests deleting an item and getting the correct response"""
        if self.inserted_item is None:
            self.test_add_item()
        item_id = self.inserted_item['_id']
        etag = self.inserted_item['_etag']
        headers = {'If-Match': etag}
        response = self.client.delete(
            'items/' + item_id, headers=headers)
        self.assertEqual(response.status_code, 204)
        inserted_item = self.items.find_one({'_id': item_id})
        self.assertEqual(inserted_item, None)
        self.inserted_item = None

    @unittest.skip('404 error handled by Eve framework')
    def test_delete_ne_item(self):
        """Tests trying to delete a non-existing item and getting a 404"""
        pass

    def test_create_order(self):
        """Tests creating an order and validates the fields in the response"""
        import json
        total = 0
        item_n = 5 # number of items in the order

        items = [] # item list in the request
        for i in range(item_n):
            item = self.items.find_one()
            quantity = random.randint(1, 5)
            items.append({
                'item': str(item['_id']),
                'quantity': quantity
            })
            total += quantity * item['price']

        request = {
            'items': items,
            'total': total,
            'note': 'made in unittests'
        }

        response = self.client.post(
            'orders', data=json.dumps(request),
            headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)

    def test_retrieving_orders(self):
        """Tests getting orders and getting the correct response"""
        response = self.client.get('orders')
        self.assertEqual(response.status_code, 200)
        json = response.json
        for i in json['_items']:
            self.assertTrue(all([k in i for k in self.order_keys]))

    def test_get_order(self):
        """Tests getting a single order and getting the correct response"""
        order = self.orders.find_one()
        response = self.client.get('orders/' + str(order['_id']))
        self.assertEqual(response.status_code, 200)
        json = response.json
        self.assertTrue(all([k in json for k in self.order_keys]))

    @unittest.skip('404 error handled by Eve framework')
    def test_get_ne_order(self):
        """Tests trying to get a non existing order and getting a 404"""
        pass
