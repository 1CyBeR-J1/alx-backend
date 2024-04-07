#!/usr/bin/env python3
""" Module that contains the class FIFICache"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ class FIFOCache that inherits from BaseCaching """

    def __init__(self):
        """Initialization of the class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
