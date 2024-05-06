#!/usr/bin/env python3
"""
This module measures the runtime of an asynchronous coroutine that runs
another coroutine multiple times concurrently
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    arg1: n - number of times to run wait_random
    arg2: max_delay - maximum delay for wait_random
    return: average execution time per run
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
