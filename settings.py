MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'apitest'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

IF_MATCH = False
PAGINATION = False

SCHEMA_ENDPOINT = 'form'

cats = {
        'item_title': 'cat',
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'schema':{
                'name': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 10,
                        'create': True,
                        'read': True,
                        'update': False
                },
                'description': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 200,
                        'create': True,
                        'read': True,
                        'update': True
                }
        }
}

dogs = {
        'item_title': 'dog',
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        'schema':{
                'name': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 10,
                        'create': True,
                        'read': True,
                        'update': False
                },
                'description': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 200,
                        'create': True,
                        'read': True,
                        'update': True
                }
        }
}

DOMAIN = {
        'cats': cats,
        'dogs': dogs
}