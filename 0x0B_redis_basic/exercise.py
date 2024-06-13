#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """
    Decorator to increment a Redis counter each time the method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_key = method.__qualname__
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Decorator to log method call arguments and results to Redis lists.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))
        return result
    return wrapper

class Cache:
    def __init__(self):
        """
        Initializes the Cache class with a Redis connection. This class is designed to interact with Redis to
        store, retrieve, and manage data along with providing utility functionalities such as logging method calls
        and maintaining a history of data operations using UUIDs for unique identification.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis under a uniquely generated UUID key. This method automatically logs the data being stored
        and the corresponding UUID key to Redis, allowing for tracking and retrieval of every instance of data storage.

        Args:
            data: Data to be stored, which can be of type str, bytes, int, or float.

        Returns:
            A UUID string that acts as the key for the stored data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Union[str, bytes, int, float, None]:
        """
        Retrieves data from Redis by the specified key. Optionally, a function can be applied to transform
        the retrieved data into a desired format, such as converting bytes to string or string to integer.

        Args:
            key: The Redis key under which the data is stored.
            fn: Optional function to apply on the retrieved data for conversion.

        Returns:
            The data retrieved from Redis, possibly converted using the provided function, or None if the key does not exist.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        return fn(value) if fn else value

    def get_str(self, key: str) -> Optional[str]:
        """
        A convenience method to directly retrieve a string from Redis. It uses the get method with a decoding function.

        Args:
            key: The Redis key to retrieve the string from.

        Returns:
            The string retrieved from Redis, or None if the key does not exist.
        """
        return self.get(key, fn=lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        A convenience method to directly retrieve an integer from Redis. It uses the get method with an integer conversion function.

        Args:
            key: The Redis key to retrieve the integer from.

        Returns:
            The integer retrieved from Redis, or None if the key does not exist.
        """
        return self.get(key, fn=int)

def replay(method: Callable):
    """
    Displays the call history of a method including input arguments and their corresponding outputs.

    Args:
        method: The method whose call history is to be displayed.

    Outputs:
        Prints each recorded call to the method along with its inputs and outputs.
    """
    method_name = method.__qualname__
    count_key = method_name
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"
    
    count = int(method.__self__._redis.get(count_key))
    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)
    
    print(f"{method_name} was called {count} times:")
    for input_str, output_str in zip(inputs, outputs):
        print(f"{method_name}(*{input_str.decode()}) -> {output_str.decode()}")
