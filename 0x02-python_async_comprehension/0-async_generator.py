#!/usr/bin/env python3
'''define a async_generator function '''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''it defines a coroutine generator function that yield
    a random number between 0 and 10'''
    for x in range(0, 10):
        await asyncio.sleep(1)
        yield(random.uniform(1, 10))
