#!/usr/bin/env python3
"""
Main file
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        method_key = method.__qualname__
        self._redis.incr(method_key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
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
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable[[bytes], Union[str, int, float]]] = None) -> Union[str, bytes, int, float, None]:
        value = self._redis.get(key)
        if value is None:
            return None
        if fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        return self.get(key, fn=lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        return self.get(key, fn=int)

def replay(method: Callable):
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
