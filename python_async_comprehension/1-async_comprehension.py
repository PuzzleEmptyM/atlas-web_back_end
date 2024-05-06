#!/usr/bin/env python3
"""
This module contains a coroutine called async_comprehension that
collects 10 random numbers asynchonously using a comprehension over
an async generator
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> list:
    """
    Asynchronously collects 10 random numbers using asynchronous comprehension
    over an async generator
    """
    return [x async for x in async_generator()]
