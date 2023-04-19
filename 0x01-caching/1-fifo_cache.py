#!/usr/bin/python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """Inherits from BaseCaching and is a caching system"""
        super().__init__()

    def put(self, key, item):
        """Assigns the item value for the key key to the cahe dictionary"""
        if key or item:
            self.cache_data[key] = item
        # Note: The dictionary is alphabetiaclly sorted
        # So first element to go in is first in the dict
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_in = list(self.cache_data.keys())[0]
            self.cache_data.pop(first_in)
            print("DISCARD:{}".format(first_in))

    def get(self, key):
        """Returns the dict value linked to key"""
        if not key and key not in self.cache.keys():
            return None
        return self.cache_data.get(key)
