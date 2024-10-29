# 0x00-pagination

## Project Overview
This project explores various pagination techniques in backend applications. It covers fundamental pagination concepts and progresses to more advanced methods, such as hypermedia pagination and deletion-resilient pagination. The project utilizes a dataset of popular baby names and demonstrates how to paginate data efficiently using different approaches.

## Learning Objectives
By the end of this project, you will be able to:
1. Paginate a dataset with basic parameters like `page` and `page_size`.
2. Use hypermedia metadata to paginate a dataset.
3. Create a pagination method that remains functional even when items are deleted.

## Requirements
- Files should be compatible with Ubuntu 18.04 LTS and Python 3.7.
- Each Python file must start with `#!/usr/bin/env python3` and end with a new line.
- Follow `pycodestyle` style (version 2.5.\*).
- Code length will be verified using `wc`.
- Each module and function should include a descriptive docstring explaining its purpose.
- All functions and coroutines must be type-annotated.

## Setup
The project uses a data file, `Popular_Baby_Names.csv`. Make sure to have this file in the directory.

## Tasks

### 0. Simple Helper Function
Write a function `index_range(page, page_size)` that returns a tuple of `(start_index, end_index)` for paginating a dataset. This is essential for identifying the range of items on a specific page.

### 1. Simple Pagination
Create a `Server` class with:
- A `dataset()` method to cache the data from `Popular_Baby_Names.csv`.
- A `get_page(page=1, page_size=10)` method that:
  - Returns the appropriate page of data using the `index_range` function.
  - Validates that `page` and `page_size` are integers greater than 0.
  - Returns an empty list if the page is out of range.

### 2. Hypermedia Pagination
Expand the `Server` class by implementing:
- A `get_hyper(page=1, page_size=10)` method that returns a dictionary containing:
  - `page_size`: the length of the returned dataset page.
  - `page`: the current page number.
  - `data`: the dataset page.
  - `next_page`: the next page number (or `None` if there isn’t one).
  - `prev_page`: the previous page number (or `None` if there isn’t one).
  - `total_pages`: the total number of pages in the dataset.
  
### 3. Deletion-Resilient Hypermedia Pagination
Implement a deletion-resilient pagination method:
- Extend the `Server` class with:
  - An `indexed_dataset()` method that indexes the dataset for efficient lookup.
  - A `get_hyper_index(index=None, page_size=10)` method that returns a dictionary with:
    - `index`: the start index of the returned page.
    - `next_index`: the index of the first item after the last item on the current page.
    - `page_size`: the current page size.
    - `data`: the page data.
- This method handles cases where items might have been removed, ensuring consistent pagination results.

## Example Usage

Example code for the tasks can be found in the following files:
- `0-simple_helper_function.py`
- `1-simple_pagination.py`
- `2-hypermedia_pagination.py`
- `3-hypermedia_del_pagination.py`

## Repository
- GitHub repository: [alx-backend](https://github.com/alx-backend)
- Directory: `0x00-pagination`
