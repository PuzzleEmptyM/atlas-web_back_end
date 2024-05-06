#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine called async_generator that
generates random numbers asynchrounosly
"""
import asyncio
import random
from collections.abc import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This coroutine loops 10 times, waits asynchronously for 1 second
    and yeilds a random number between 0 and 10 each iteration

    return: AsyncGenerator[float, None]
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10)  # Yield a random number between 0 and 10
