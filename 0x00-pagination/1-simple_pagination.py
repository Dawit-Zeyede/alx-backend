#!/usr/bin/env python3
'''
get_page.
'''
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Returns a tuple of size two containing a start index and end index.
    '''
    staIndex = (page - 1) * page_size
    endex = staIndex + page_size
    return (staIndex, endex)


class Server:
    '''
    Server class to paginate a database of popular baby names.
    '''
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        Initializes a new Server instance.
        '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        '''
        Cached dataset
        '''
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        takes two integer arguments and return data value.
        '''
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        staIndex, endex = index_range(page, page_size)
        data = self.dataset()
        if staIndex > len(data):
            return []
        return data[staIndex:endex]
