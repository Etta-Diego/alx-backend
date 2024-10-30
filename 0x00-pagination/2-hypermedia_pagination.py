#!/usr/bin/env python3

"""
Adds `get_hyper` method to `Server` class
"""

import csv
import math
from typing import List, Tuple, Dict, Any


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Get pages details and items
        Args:
            page_size: the length of the returned dataset page
            page: the current page number
        Returns:
            A dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page (equivalent to return from previous task)
            next_page: number of the next page, None if no next page
            prev_page: number of the previous page, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """

        assert isinstance(page_size, int) and page_size > 0
        assert isinstance(page, int) and page > 0

        data = self.get_page(page, page_size)
        page_size = len(data)
        total_pages = math.ceil(len(data) / page_size) if page_size > 0 else 0
        next_page = page + 1 if page < total_pages else None
        prev_page = page + 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
