#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that runs another coroutine
multiple times concurrently.
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    arg1: n - number of times to run wait_random.
    arg2: max_delay - maximum delay for wait_random.
    return: a list of float values representing the delays
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed_delays.append(delay)
    return completed_delays
