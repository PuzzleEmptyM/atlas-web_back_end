#!/usr/bin/env python3
"""
FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements FIFO caching policy
    """
    def __init__(self):
        """
        Initialize the FIFOCache class with an empty cache
        """
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Assign item value for the key in the cache dict
        Follows FIFO policy for evicting items if cache exceeds MAX_ITEMS
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    first_in_key = self.key_order.pop(0)
                    del self.cache_data[first_in_key]
                    print(f"DISCARD: {first_in_key}")
                self.cache_data[key] = item
                self.key_order.append(key)

    def get(self, key):
        """
        Return value linked to key from cache_data
        Return None if key is None or key doesn't exist
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
