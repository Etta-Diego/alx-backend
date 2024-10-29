#!/usr/bin/env python3

"""
index_range: Function that takes two integer arguments
page and page_size.

"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start index and the end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters.
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        a tuple of the start and end index for the given page
    """

    start_page = (page - 1) * page_size

    end_page = page * page_size

    tuple_range = (start_page, end_page)
    return tuple_range
