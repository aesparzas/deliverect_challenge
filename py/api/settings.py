MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
MONGO_DBNAME = 'orders'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

items = {
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'description'
    },
    'schema': {
        'description': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required': True,
            'unique': True
        },
        'quantity': {
            'type': 'number',
            'required': True
        },
        'price': {
            'type': 'number',
            'required': True
        }
    }
}

orders = {

}

DOMAIN = {
    'items': items,
    'orders': orders
}