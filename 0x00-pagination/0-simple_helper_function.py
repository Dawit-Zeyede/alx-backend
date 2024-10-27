#!/usr/bin/env python3
'''
Simple helper function.
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns a tuple of size two containing a start index and end index.
    '''
    staIndex = (page - 1) * page_size
    endex = staIndex + page_size
    return (staIndex, endex)
