#!/usr/bin/env python3
'''defines sum_mixed_list takes a mixed list '''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    '''takes a list of mixed of int and float and return a float'''
    return float(sum(mxd_list))
