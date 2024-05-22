#!/usr/bin/env python3

"""Import the base_cache class"""

BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system"""

    def put(self, key, item):
        """Add an item in the cache, and removes the first
        pair in the dict and prints the the removed key"""
        value = self.cache_data.values()
        value_length = len(value)

        if value_length > BaseCaching.MAX_ITEMS:
            first_key, first_value = next(iter(self.cache_data.items()))
            deleted_key = self.cache_data.pop(first_key, first_value)
            print("Discard: {}".format(first_key))

        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key in self.cache_data is None:
            return None

        return self.cache_data.get(key)
