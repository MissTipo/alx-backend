#!/usr/bin/env python3
"""
FIFO    caching
[]      put(A)  -
[A]     put(B)  -
[AB]    put(C)  -
[ABC]   put[D]  -
[ABCD]  put(E)  pop(A)
[BCDE]  put(C)  -
[BDEC]  put(F)  pop(B)
[[DECF]]
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system"""
    def __init__(self):
        """Inherits from BaseCaching and is a caching system"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Assigns the item value for the key key to the cahe dictionary"""
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            elif len(self.cache_data) < self.MAX_ITEMS:
                self.cache_data[key] = item
                self.keys.append(key)
            else:
                # first_in = list(self.cache_data.keys())[0]
                first_in = self.keys.pop(0)
                print("DISCARD: {}".format(first_in))
                self.cache_data.pop(first_in)
                self.cache_data[key] = item
                self.keys.append(key)

    def get(self, key):
        """Returns the dict value linked to key"""
        if (key is None) or (key not in self.cache_data):
            return None
        return self.cache_data[key]
