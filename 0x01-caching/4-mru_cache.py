#!/usr/bin/env python3

"""Import the base_cache class"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """MRUCache is a caching system"""

    def __init__(self):
        """Initialize the LRUCache"""
        super().__init__()
        """List to maintain the order of keys"""
        self.order = []

    def put(self, key, item):
        """Add an item in the cache, and removes the most recent used
        pair in the dict and prints the the removed key"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            """Move the existing key to the end
            to mark it as recently used"""
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            """Remove the most recent used key added"""
            most_used_key = self.order.pop(-1)
            del self.cache_data[most_used_key]
            print("DISCARD: {}".format(most_used_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Get an item by key"""
        if key is None or key in self.cache_data is None:
            return None

        return self.cache_data.get(key)
