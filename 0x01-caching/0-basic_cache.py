#!/usr/bin/python3
"""Basic cache dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""

    def put(self, key, item):
        if key or item:
            self.cache_data[key] = item

    def get(self, key):
        """Returns the dic value linked to the key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
