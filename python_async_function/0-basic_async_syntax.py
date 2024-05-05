#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine that waits for a random time
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    arg: max_delay - max delay, defaults to 10
    return: float - random delay duration
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
