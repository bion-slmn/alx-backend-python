#!/usr/bin/env python3
'''defines a function make_multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''func take a float and returns a function that multiplies the
    multiplier with a float'''
    def another_func(m2: float) -> float:
        '''mutipliers the args of make_multiplier to m2'''
        return float(m2 * multiplier)
    return another_func
