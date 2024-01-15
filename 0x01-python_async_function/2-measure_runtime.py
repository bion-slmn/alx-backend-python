#!/usr/bin/env python3
'''defines a function measure_time'''
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' measures the time taken for the function to execute wait_n
    and return the average exection time for n times'''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return (end - start) / n
