#!/usr/bin/env python3
"""
This script tests the task_wait_n function by running it and printing
the results
"""
import asyncio
task_wait_n = __import__('4-tasks').task_wait_n


n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
