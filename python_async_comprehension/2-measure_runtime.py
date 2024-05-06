#!/usr/bin/env python3
"""
This module contains a coroutine called measure_runtime that measures
the total runtime of executing the async_comprehension coroutine four
times in parallel
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures and returns the total runtime of executing async_comprehension
    four times in parallel

    return: float - the total runtime in seconds
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    return end_time - start_time
