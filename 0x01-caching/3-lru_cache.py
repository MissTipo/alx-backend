#!/usr/bin/env python3
"""LRU Caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
                # self.keys.append(key)
                # self.cache_data[key] = item
            elif len(self.cache_data) >= self.MAX_ITEMS:
                least_used = self.keys.pop(0)
                del self.cache_data[least_used]
                print("DISCARD: {}".format(least_used))
            self.keys.append(key)
            self.cache_data[key] = item
            """else:
                least_used = self.keys.pop(0)
                del self.cache_data[least_used]
                print("DISCARD: {}".format(least_used))
                self.cache_data[key] = item
                self.keys.append(key)"""

    def get(self, key):
        """Returns the dictionary value linked to the key"""
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache_data[key]
            return self.cache_data[key]
        # return self.cache_data.get(key)
