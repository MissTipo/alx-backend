#!/usr/bin/env python3
"""Basic cache dictionary"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key or item:
            self.cache_data[key] = item
        return

    def get(self, key):
        """Returns the dictionary value linked to the key"""
        if (key is None) or (key not in self.cache_data):
            return None
        if key in self.cache_data:
            return self.cache_data[key]
