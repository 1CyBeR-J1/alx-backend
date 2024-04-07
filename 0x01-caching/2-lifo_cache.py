#!/usr/bin/env python3
""" Module that contains LIFOcache class"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class LIFOCache that inherits from BaseCaching """

    def __init__(self):
        """ Initialization of the class """
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the
        item value for the key key

        Args:
                        key (_type_): _description_
                        item (_type_): _description_
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                # delete the last item in the dictionary
                last_key, last_value = self.cache_data.popitem()
                print("DISCARD: {}". format(last_key))

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key

        Args:
                        key (_type_): _description_
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
