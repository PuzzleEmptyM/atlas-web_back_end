#!/usr/bin/env python3
"""
FIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache class inherits from BaseCaching and implements LIFO caching
    """
    def __init__(self):
        """
        Initialize LIFOCache class with empty cache and ist to track insertion
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Store the item in cache_data using provided key
        Follows LIFO policy for evicting items if exceeds MAX_ITEMS
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key in self.key_order:
                self.key_order.remove(key)
            self.key_order.append(key)
            if len(self.cache_data) > self.MAX_ITEMS:
                last_in_key = self.key_order.pop(-2)
                del self.cache_data[last_in_key]
                print(f"DISCARD: {last_in_key}")

    def get(self, key):
        """
        Return value linked to key from cache_data
        Returns None if key is None or key does not exist in cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
