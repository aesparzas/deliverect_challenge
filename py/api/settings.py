MONGO_HOST = 'mongodb'
MONGO_PORT = 27017
MONGO_DBNAME = 'orders'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']

items = {
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
    'resource_methods': ['GET', 'POST'],
    'item_methods': ['GET'],
    'schema': {
        'items': {
            'type': 'list',
            'schema': {
                'type': 'dict',
                'schema': {
                    'item': {
                        'type': 'objectid',
                    },
                    'quantity': {
                        'type': 'integer'
                    }
                }
            },
            'required': True
        },
        'total': {
            'type': 'number',
            'required': True
        },
        'note': {
            'type': 'string',
            'maxlength': 50
        }
    }
}

DOMAIN = {
    'items': items,
    'orders': orders
}
