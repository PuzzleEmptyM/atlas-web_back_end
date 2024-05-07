#!/usr/bin/env python3
"""
A class BasicCache that inherits from BaseCaching and is a caching system
"""


class BaseCaching:
    """
    Base caching class with basic methods to manage caching
    """
    def __init__(self):
        self.cache_data = {}

    def print_cache(self):
        print("Current cache:")
        for key in self.cache_data:
            print(f"{key}: {self.cache_data[key]}")


class BasicCache(BaseCaching):
    """
    BasicCache class inherits from BaseCaching and provides simple
    """
    def put(self, key, item):
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        if key is not None or key not in self.cache_data:
            return None
        return self.cache_data[key]
