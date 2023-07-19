#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class
    """
    def __init__(self):
        """ Constructor method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that takes a data argument and returns a string
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None)\
            -> Union[str, bytes, int, float]:
        """ Method that takes a key string argument and an optional
            Callable argument named fn and returns a value
        """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """ Method that will automatically parametrize Cache.get
            with the correct conversion function
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Method that will automatically parametrize Cache.get
            with the correct conversion function
        """
        return self.get(key, int)