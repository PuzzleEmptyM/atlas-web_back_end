#!/usr/bin/env python3
"""
LRU caching module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache class inherits from BaseCaching and implements LRU caching policy
    """
    def __init__(self):
        """
        INitialize LRUCache class with empty cache and list to track order
        """
        super().__init__()
        self.usage_order = []

    def put(self, key, item):
        """
        Store item in cache_data using provided key
        If cache exceeds MAX_ITEMS, discards least recently used
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.usage_order.remove[key]
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    lru_key = self.usage_order.pop(0)
                    del self.cache_data[lru_key]
                    print(f"DISCARD: {lru_key}")
                self.cache_data[key] = item
                self.usage_order.append(key)

    def get(self, key):
        """
        Return value linked to key from cache_data
        Moves key to end of useage list to mark as recently used
        Returns None if key is None or not in cache_data
        """
        if key is None or key not in self.cache_data:
            return None
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
