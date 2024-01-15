#!/usr/bin/env python3
'''defines a task_wait_random sync function'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    ''' function return a task '''
    return asyncio.create_task(wait_random(max_delay))
