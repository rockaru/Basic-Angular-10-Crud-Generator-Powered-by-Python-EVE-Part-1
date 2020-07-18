from eve import Eve
from eve.io.mongo import Validator

class MyValidator(Validator):
        def _validate_create(self):
                """ {'type': 'boolean'} """
                pass
        def _validate_read(self):
                """ {'type': 'boolean'} """
                pass
        def _validate_update(self):
                """ {'type': 'boolean'} """
                pass

app = Eve(validator=MyValidator)

if __name__ == '__main__':
        app.run()