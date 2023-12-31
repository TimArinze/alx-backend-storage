#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs
    for a particular function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.rpush("{}:inputs".format(key), str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush("{}:outputs".format(key), str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a single method Callable argument and returns
    a Callable"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Wrapper function"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def replay(method: Callable):
    """function to display the history of calls of a particular function"""
    key = method.__qualname__
    r = redis.Redis()
    inputs = r.lrange("{}:inputs".format(key), 0, -1)
    outputs = r.lrange("{}:outputs".format(key), 0, -1)

    print("{} was called {} times:".format(key, r.get(key).decode("utf-8")))
    for i, o in zip(inputs, outputs):
        input = i.decode("utf-8")
        output = o.decode("utf-8")
        print("{}(*{}) -> {}".format(key, input, output))


class Cache:
    """Writing strings to Redis"""
    def __init__(self):
        """Constructor method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Method that takes a data argument and returns a string"""
        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str, fn: Callable = None):
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
