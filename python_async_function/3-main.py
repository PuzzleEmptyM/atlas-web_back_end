#!/usr/bin/env python3
"""
This script demonstrates creating and using an asyncio.Task.
"""
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> None:
    """
    arg1: max_delay - max delay to pass to task_wait_random
    function.
    """
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)


# Run the test coroutine
asyncio.run(test(5))
