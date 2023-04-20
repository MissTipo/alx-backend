#!/usr/bin/env python3
"""LIFO Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""

    def __init__(self):
        """Instantiates LIFOCache"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Assigns the item value for the key key to the cache dictionary"""
        # if key or item:
        # self.cache_data[key] = item
        if key and item:
            if key in self.cache_data:
                self.cache_data.pop(key)
                self.keys.append(key)
                self.cache_data[key] = item
            elif len(self.cache_data) < self.MAX_ITEMS:
                self.keys.append(key)
                self.cache_data[key] = item
            else:
                last_in = self.keys.pop(-1)
                del self.cache_data[last_in]
                print("DISCARD: {}".format(last_in))
                self.cache_data[key] = item
                self.keys.append(key)

    def get(self, key):
        """Returns the dictionary value linked to the key"""
        if not key and key not in self.cache_data.keys():
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        # return self.cache_data.get(key)
