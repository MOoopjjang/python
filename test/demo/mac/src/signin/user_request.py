#!python3
# -*- coding:utf -*-


from src.common.domain.base_domain import BaseDomain


class UserRequest(BaseDomain):
    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username
