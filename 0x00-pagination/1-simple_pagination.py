#!/usr/bin/env python3

"""
Implement get_page that takes two integer arguments page with
default value 1 and page_size with default value 10.
"""

import csv
import math
from typing import List, Tuple


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[list]:

        """
        Get items for the given page number
        Args:
            page (int): page number
            page_size (int): number of items per page
        Returns:
            a list of list(row) if inputs are within range
            ([]) : an empty list if page and page_size are out of range
        """
        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0

        dataset_len = len(self.dataset())

        start_indx, end_indx = index_range(page, page_size)

        if start_indx >= dataset_len:
            return []

        return self.dataset()[start_indx:end_indx]
