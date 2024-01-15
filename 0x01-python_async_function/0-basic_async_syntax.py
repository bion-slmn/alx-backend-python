#!/usr/bin/env python3
'''this module defines a wait_random async function'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''this waits for a random delay in seconds and returns
    the random delay'''
    delay_time = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)

    return delay_time
