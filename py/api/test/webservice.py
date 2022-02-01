import unittest


class TestWebservice(unittest.TestCase):
    def setUp(self):
        pass

    def test_retrieve_items(self):
        """Tests retrieving a list of items and getting the correct response"""
        pass

    def test_filtering_items(self):
        """Tests filtering a list of items and getting the correct response"""
        pass

    def test_get_item(self):
        """Tests getting an item and getting the correct response"""
        pass

    def test_get_not_found_item(self):
        """Tests getting an non-existing item and getting a 404"""
        pass

    def test_add_item(self):
        """Tests adding an item and getting the correct response"""
        pass

    def test_add_item_missing(self):
        """Tests trying to add an item with missing params and getting a 400"""
        pass

    def test_update_item(self):
        """Tests updating an item and getting the correct response"""
        pass

    def test_update_ne_item(self):
        """Tests trying to update a non-existing item and getting a 404"""
        pass

    def test_delete_item(self):
        """Tests deleting an item and getting the correct response"""
        pass

    def test_delete_ne_item(self):
        """Tests trying to delete a non-existing item and getting a 404"""
        pass

    def test_create_order(self):
        """Tests creating an order and validates the fields in the response"""
        pass

    def test_retrieving_orders(self):
        """Tests getting orders and getting the correct response"""
        pass

    def test_get_order(self):
        """Tests getting a single order and getting the correct response"""
        pass

    def test_get_ne_order(self):
        """Tests trying to get a non existing order and getting a 404"""
        pass
