#!/usr/bin/env python3
'''defines and duck types the function beloow'''
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''takes any sequence and returns first element or none'''
    if lst:
        return lst[0]
    return None
