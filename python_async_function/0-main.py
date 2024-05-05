#!/usr/bin/env python3
"""
This script demonstrates the use of the wait_random coroutine.
"""
import asyncio


# Import the wait_random function from the 0-basic_async_syntax module
wait_random = __import__('0-basic_async_syntax').wait_random


# Using asyncio.run to execute the coroutine and print the results
print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
