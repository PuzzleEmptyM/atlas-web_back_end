#!/usr/bin/env python3
"""
This module contains an asynchronous coroutine called async_generator that
generates random numbers asynchronously.
"""
import asyncio
import random
from typing import AsyncGenerator  # Ensure you're using Python 3.9 or newer


async def async_generator() -> AsyncGenerator[float, None]:
    """
    This coroutine loops 10 times, waits asynchronously for 1 second,
    and yields a random number between 0 and 10 each iteration.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
