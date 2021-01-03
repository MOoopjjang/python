#!python3
#-*- coding:utf -*-


import json

class UserRequest:
    def __init__(self , email , password , username ):
        self.email = email
        self.password = password
        self.username = username

    def toJSON(self):
        return json.dumps(self.__dict__)
