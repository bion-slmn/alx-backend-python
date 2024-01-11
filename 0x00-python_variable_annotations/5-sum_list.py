#!/usr/bin/env python3
'''defines a type annotated function sum_list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''takes a list of afloats and sums them to return a float'''
    return sum(input_list)
