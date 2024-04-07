#!/usr/bin/env python3
""" Module that contains the BasicCache method"""


BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A parent class that is a caching system"""

    def __init__(self):
        """Initialization of the method"""
        super().__init__()

    def put(self, key, item):
        """Assigns

        Args:
                key (_type_): _description_
                item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
