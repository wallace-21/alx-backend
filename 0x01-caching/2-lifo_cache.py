#!/usr/bin/env python3

"""Import the base_cache class"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system"""

    def __init__(self):
        """Initialize the FIFOCache"""
        super().__init__()
        """List to maintain the order of keys"""
        self.order = []

    def put(self, key, item):
        """Add an item in the cache, and removes the last
        pair in the dict and prints the the removed key"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """Remove the last key added"""
                last_key = self.order.pop(-1)
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

        self.cache_data[key] = item
        if key not in self.order:
            self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key in self.cache_data is None:
            return None

        return self.cache_data.get(key)
