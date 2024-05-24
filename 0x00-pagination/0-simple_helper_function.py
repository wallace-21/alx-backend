#!/usr/bin/env python3

"""import typing to set types"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ unction, you need to calculate the start and
    end indexes for the given page and page_size"""

    start_index: int = (page - 1) * page_size
    end_index: int = start_index + page_size
    indexes: Tiple(int) = (start_index, end_index)
    return (indexes)
