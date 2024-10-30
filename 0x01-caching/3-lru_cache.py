#!/usr/bin/python3
""" Module for LRUCache """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initialize cache with parent init and an order tracker list """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add item to cache using LRU eviction policy """
        if key is None or item is None:
            return

        # Add or update the item in cache and track the order of usage
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item if cache is full
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Retrieve an item from the cache by key"""
        if key is None or key not in self.cache_data:
            return None
        # Update the order to mark this key as recently used
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
