#!/usr/bin/python3
""" Module for LFUCache """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache class implementing LFU caching system """

    def __init__(self):
        """Initialize LFUCache with parent init, frequency n usage tracking"""
        super().__init__()
        self.frequency = {}
        self.usage_order = []

    def put(self, key, item):
        """ Add an item to the cache using LFU eviction policy """
        if key is None or item is None:
            return

        # Update the cache and usage frequency if the item already exists
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.remove(key)
            self.usage_order.append(key)
        else:
            # Evict if cache size exceeds MAX_ITEMS
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.evict_lfu()
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order.append(key)

    def evict_lfu(self):
        """ Evict the least frequently used item;
        if a tie, evict the least recently used one """
        # Find the minimum frequency in the frequency dictionary
        min_freq = min(self.frequency.values())
        # Candidates for eviction: all items with minimum frequency
        candidates = [
            key for key in self.usage_order if self.frequency[key] == min_freq
        ]
        # The first item in the order list is the LRU
        lfu_key = candidates[0]

        # Remove the item from cache, frequency, and usage tracking
        self.cache_data.pop(lfu_key)
        self.frequency.pop(lfu_key)
        self.usage_order.remove(lfu_key)
        print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """Retrieve item from cache by key and update frequency and order """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and move key to the end to mark it as recently used
        self.frequency[key] += 1
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
