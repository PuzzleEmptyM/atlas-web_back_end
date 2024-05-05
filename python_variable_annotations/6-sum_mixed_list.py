#!/usr/bin/env python3
"""
A function to compute the sum of a list of mixed integers and floats
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    arg: (List[Union[int, float]]) - input list of mixed integers
    return: float - sum of input list
    """
    return sum(mxd_lst)
