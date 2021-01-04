#!python3
# -*- coding:utf-8 -*-


class UserResponse:
    def __init__(self, email, token, refreshToken):
        self.email = email
        self.token = token
        self.refreshToken = refreshToken
