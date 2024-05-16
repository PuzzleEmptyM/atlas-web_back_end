#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments page and
page_size. The function should return a tuple of size two containing a start
index and an end index correspoding to the range of indexes to return in a list
for those particular pagination paramaters.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Arg1: page - int
    Arg2: page_size - int
    Return: tuple containing start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
