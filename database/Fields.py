'''
Implementations of special subclasses for Peewee fields.
See API documentation for details on methods being overriden.
'''
from peewee import *


class ListField(TextField):
    '''
    Overrides certain methods of Peewee's TextField to store python lists
    appropriately in th database.
    
    db_value: concatenates and saves list as text
    python_value: returns combined text list to Python list object

    Reference: https://groups.google.com/forum/#!topic/peewee-orm/if3CcSKFVYg
    '''
    
    def db_value(self, value):
        if value:
            value = ','.join(value)
        else:
            print('ERROR: ListField only accepts lists')
        
        return value

    def python_value(self, value):
        return value.split(',')