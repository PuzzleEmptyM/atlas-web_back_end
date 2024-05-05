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
    Runs wait_random n times concurrently with the specified max_delay and
    returns a list of delays.
    Args:
    n (int): The number of times to run wait_random.
    max_delay (int): The maximum delay for wait_random.
    Returns:
    List[float]: A list of float values representing the delays, ordered
    naturally by concurrency.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed_delays.append(delay)
    return completed_delays
