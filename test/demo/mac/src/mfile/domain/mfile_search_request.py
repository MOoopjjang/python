#!python3
# -*- coding:utf-8 -*-


from src.common.domain.base_domain import BaseDomain


class MFileSearchRequest( BaseDomain ):
    def __init__(self , _type , _value , _p = 0 , _s = 10):
        self.searchType = _type
        self.searchValue= _value
        self.currentPage = _p
        self.size = _s





