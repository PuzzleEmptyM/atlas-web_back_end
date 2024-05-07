#!/usr/bin/env python3
"""
A class BasicCache that inherits from BaseCaching and is a caching system
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class inherits from BaseCaching and provides simple
    """
    def put(self, key, item):
        """
        Store item in cache_data using provided key
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Return item linked to key from cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
