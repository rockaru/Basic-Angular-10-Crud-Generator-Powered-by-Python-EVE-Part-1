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
        'cache_control': 'max-age=0,must-revalidate',
        'cache_expires': 1,
        'schema':{
                'name': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 10,
                        'input':'text'
                        'create': True,
                        'read': True,
                        'update': False,
                        'delete':True,
                        'detail':True
                },
                'description': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 200,
                        'input':'textarea',
                        'create': True,
                        'read': True,
                        'update': True,
                        'delete':True,
                        'detail':True
                }
        }
}

dogs = {
        'item_title': 'dog',
        'cache_control': 'max-age=0,must-revalidate',
        'cache_expires': 1,
        'schema':{
                'name': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 10,
                        'input':'text',
                        'create': True,
                        'read': True,
                        'update': False,
                        'delete':True,
                        'detail':True
                },
                'description': {
                        'type': 'string',
                        'minlength': 1,
                        'maxlength': 200,
                        'input':'textarea',
                        'create': True,
                        'read': True,
                        'update': True,
                        'delete':True,
                        'detail':True
                }
        }
}

DOMAIN = {
        'cats': cats,
        'dogs': dogs
}