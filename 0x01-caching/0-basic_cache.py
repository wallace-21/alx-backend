#!/usr/bin/env python3

"""Import the base_cache class"""

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key in self.cache_data is None:
            return None

        return self.cache_data.get(key)
