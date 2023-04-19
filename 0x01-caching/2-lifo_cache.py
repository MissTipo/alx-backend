#!/usr/bin/python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Instantiates LIFOCache"""
        super().__init__()
    def put(self, key, item):
        """Assigns the item value for the key key to the cache dictionary"""
        #if key or item:
            #self.cache_data[key] = item
        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data.pop(key)
            else:
                # last_in = list(self.cache_data.keys())[-1]
                key1, value = self.cache_data.popitem()
                print("DISCARD: {}".format(key1))
        if key or item and key not in self.cache_data.keys():
            self.cache_data[key] = item

    def get(self, key):
        """Returns the dictionary value linked to the key"""
        if not key and key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)

