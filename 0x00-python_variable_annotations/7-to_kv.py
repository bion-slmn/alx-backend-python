#!/usr/bin/env python3
'''defines a type annotated function to_kv '''
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''take a string and either int or float and returns a
    tuple with the first element a string and the second a float by
    squaring the second arg'''
    return (k, float(v**2))
