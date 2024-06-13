#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

# Define the count_calls decorator that enhances methods with call count tracking
def count_calls(method: Callable) -> Callable:
    """
    A decorator that counts the number of times a method is called, using Redis.
    The count for each method is stored in Redis under a key that includes
    the method's qualified name using the __qualname__ attribute.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Construct the key using the method's qualified name
        method_key = f"count:{method.__qualname__}"
        # Increment the method call count in Redis
        self._redis.incr(method_key)
        # Call the original method and return its result
        return method(*args, **kwargs)
    return wrapper

class Cache:
    def __init__(self):
        # Initialize the Redis connection
        self._redis = redis.Redis()
        self._redis.flushdb()  # Clear any existing data in Redis

    @count_calls  # Decorate the store method to count its invocations
    def store(self, data: Union[str, bytes, int, float]) -> str:
        # Generate a unique key for storing the data
        key = str(uuid.uuid4())
        # Store the data in Redis under the generated key
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Union[str, bytes, int, float, None]:
        # Retrieve data from Redis by key
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            # If a conversion function is provided, apply it to the data
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        # Helper method to get a string from Redis
        return self.get(key, fn=lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        # Helper method to get an integer from Redis
        return self.get(key, fn=int)
