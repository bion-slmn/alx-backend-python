#!/usr/bin/env python3
'''defines a function async_compreshension'''
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''this coroutine, iterates over an async generator function
    and returns a the results using async comprehension'''
    return [i async for i in async_generator()]
