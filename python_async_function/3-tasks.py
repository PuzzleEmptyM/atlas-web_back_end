#!/usr/bin/env python3
"""
This module contains a function that wraps a coroutine into a
coroutine into an asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    arg1: max_delay - max delay for wait_random
    return: asyncio.Task - task object associated with coroutine
    """
    return asyncio.create_task(wait_random(max_delay))
