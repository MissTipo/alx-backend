#!/usr/bin/env python3
"""Basic cache dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the dictionary value linked to the key"""
        if not key and key not in self.cache_data.keys():
            return None
        if key in self.cache_data:
            return self.cache_data[key]
        # return self.cache_data.get(key)


    """def get(self, key):
        Returns the dic value linked to the key
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)"""
