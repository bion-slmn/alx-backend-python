#!/usr/bin/env python3
'''type checking with mypy'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''returns a tuple'''
    zoomed_in: List = [item for item in lst for i in range(factor)]
    return zoomed_in


tupl = (12, 72, 91)

zoom_2x = zoom_array(tupl)

zoom_3x = zoom_array(tupl, 3)
