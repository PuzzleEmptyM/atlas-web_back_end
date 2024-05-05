#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that runs another coroutine
multiple times concurrently.
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """
    Runs wait_random n times concurrently with the specified max_delay.

    Args:
    n (int): The number of times to run wait_random.
    max_delay (int): The maximum delay for wait_random.

    Returns:
    list: A list of float values representing the delays, ordered naturally
    by concurrency.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed_delays.append(delay)
    return completed_delays
