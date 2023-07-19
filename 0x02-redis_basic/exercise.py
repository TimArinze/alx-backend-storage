#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """Writing strings to Redis"""
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    def store(self, data: Union[float, str, int, bytes]) -> str:
        """Method that takes a data argument and returns a string"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
