#!/usr/bin/env python3
"""
This module contains a coroutine that runs another coroutine multiple times
concurrently, wrapping each call into a task
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_def__n(n: int, max_delay: int) -> List(float):
    """
    arg1: n - number of times to run task_ wait_random
    arg2: max_delay - maximum delay for task_wait_random
    return: list of float values representing delays, ordered by concurrency
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    completed_delays = []
    for task in asyncio.as_completed(tasks):
        delay = await task
        completed_delays.append(delay)
    return completed_delays
