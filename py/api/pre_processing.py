"""
Pre processing functions needed to keep coherent data
"""
from pymongo import MongoClient


class PreProcessingException(Exception):
    issues = dict()


def create_order(items):
    """
    When an order is created, the unitary price of each item in the order should be
    fetched and multiplied by the quantity detailed in the request. This will avoid
    that if prices on items are changed in the future, consistency fails.

    After having that done, the order total should be calculated and compared with
    the total sent in the body. If the totals differ, the operation is aborted
    """
    mongo_client = MongoClient('mongodb', 27017)
    db = mongo_client['orders']
    db_items = db.items

    for e in items:
        total = 0
        for item in e['items']:
            db_item = db_items.find_one({'_id': item['item']})
            if not db_item: # if the item doesn't exist in db, raise exception
                exception = PreProcessingException
                exception.issues = {"items": "some of the items doesn't exist in db"}
                raise exception
            price = db_item['price']
            subtotal = price * item['quantity']
            total += subtotal
            item['subtotal'] = subtotal
        if total != e['total']: # if calculated total differs to the one sent
            exception = PreProcessingException
            exception.issues = {"total": "error in total calculation"}
            raise exception



