#!/usr/bin/env python3

'''Task 0: The first task on the Basic dictionary
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits frm `BaseCaching`
       n is a caching system
    '''

    def put(self, key, item):
        '''assigning to the dictionaary `self.cache_data` the
           `item` value for the key `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''returning the value in `self.cache_data` linked to `key`
        '''

        return self.cache_data.get(key, None)
