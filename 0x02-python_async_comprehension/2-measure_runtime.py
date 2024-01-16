#!/usr/bin/env python3
'''defines a function measure time'''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures the time taken for 4 coroutines'''
    start = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()

    return end - start
