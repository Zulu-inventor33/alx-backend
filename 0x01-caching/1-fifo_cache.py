#!/usr/bin/python3
""" Module for FIFOCache """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """ Initialize the cache with the parent init"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item to the cache using FIFO eviction policy """
        if key is None or item is None:
            return

        # Add or update the item in cache and track the insertion order
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Remove the oldest item (FIFO) if cache is full
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")
            self.order.append(key)
        else:
            # Update the order for an existing key
            self.order.remove(key)
            self.order.append(key)

        self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
