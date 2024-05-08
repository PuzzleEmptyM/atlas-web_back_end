#!/usr/bin/env python3
"""
MRU caching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache class inherits from BaseCahing and implements MRU caching policy
    """
    def __init__(self):
        """
        Initialize the MRUCache class with empty cache and list to track order
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Store item in cache_data using the provided key
        If cache exceeds MAX_ITEMS, discards  most recently used item
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item
            self.usage_order.append(key)

    def get(self, key):
        """
        Return value linked to key from cache_data
        Move key to end of usage list to mark as recently used
        Return None if key is None or not in cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
