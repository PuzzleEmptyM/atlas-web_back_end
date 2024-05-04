#!/usr/bin/env python3
"""
a type-annotated function floor which takes a float n as argument and returns
the floor of the float.
"""
import math


def floor(n: float) -> int:
    """
    arg: n - number
    return: the floor of that number
    """
    return math.floor(n)
