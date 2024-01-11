#!/usr/bin/env python3
'''using type var for dictionary'''
from typing import TypeVar, Mapping, Union, Any


T = TypeVar('T')
v = TypeVar('v')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''using mapping to indicate the dict is read only'''
    if key in dct:
        return dct[key]
    return default
