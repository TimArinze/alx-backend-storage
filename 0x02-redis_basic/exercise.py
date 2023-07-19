#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """Writing strings to Redis"""
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes a data argument and returns a string"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable =None):
        """Reading from Redis and recovering original type"""
        if key is None:
            return None
        if fn:
            return fn(self._redis.get(key))
        else:
            return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Reading from Redis and recovering original type"""
        return str(self.get(key))
    
    def get_int(self, key: str) -> int:
        """Reading from Redis and recovering original type"""
        return int(self.get(key))
    