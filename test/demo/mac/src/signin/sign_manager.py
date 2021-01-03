#!python3
#-*- coding:utf-8 -*-


from src.signin.user_request import UserRequest
from src.signin.user_response import UserResponse
from src.common.singleton_decorator import SingletonDecorator
import src.common.common_util as cutil
import src.common.defines as df
import requests
import json


@SingletonDecorator(tag = "[SM]" , dp = True)
class SignManager:
    def signup(self , email , password , username , _successFunc = None , _failFunc = None):
        userRequest = UserRequest(email , password , username)
        res = requests.post(df.SIGNIN_URI , data=userRequest.toJSON(), headers = cutil.getDefaultHeader())
        responseData = res.json()
        # print(f'result : {responseData}')
        if(_successFunc != None and _failFunc != None):
            if responseData['result'] == 'OK':
                _successFunc(responseData['body'])
            else:
                _failFunc(responseData)



