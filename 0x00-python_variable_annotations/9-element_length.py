#!/usr/bin/env python3
''' defines a fucntion element_length'''
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''takes a iterable which consists of sequence and returns a list of
    tuple'''
    return [(i, len(i)) for i in lst]
