#!python3
#-*- coding:utf -*-

from src.common.domain.base_domain import BaseDomain


class CategoryRequest( BaseDomain ):
    def __init__(self , _name , _cd ):
        self.cateName = _name
        self.cateCd = _cd
