#!/usr/bin/env python3
"""
A function to create a multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    arg: multiplier
    return: the result of multiplication
    """
    def multiplier_function(x: float) -> float:
        """
        arg: x - input float
        return: result of multiplying x by multiplier
        """
        return x * multiplier
    return multiplier_function
