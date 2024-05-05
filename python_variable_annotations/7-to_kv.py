#!/usr/bin/env python3
"""
A function to create a tuple where the first element is a string
and the second element is the square of an int or float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    arg1: k - input string
    arg2: v - input integer or float
    return: tuple containing input string and square of input
    """
    return (k, v * v)
