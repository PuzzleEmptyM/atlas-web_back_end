#!/usr/bin/env python3
"""
A function to calculate the length of elements in a list
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    arg: 1st - input list
    return: list where each tuple contains element from input list
    """
    return [(i, len(i)) for i in lst]
