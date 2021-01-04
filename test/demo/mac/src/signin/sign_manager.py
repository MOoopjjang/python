#!python3
# -*- coding:utf-8 -*-


from src.signin.user_request import UserRequest
from src.common.singleton_decorator import SingletonDecorator
import src.common.httpheader_util as hhutil
import src.common.defines as df
from src.common.network_manager import NetworkManager
from src.common.authentication_manager import AuthenticationManager


@SingletonDecorator(tag="[SM]", dp=True)
class SignManager:
    def signup(self, email, password, username):
        userRequest = UserRequest(email, password, username)
        NetworkManager().post(df.SIGNIN_URI
                              , data=userRequest.toJSON()
                              , headers=hhutil.getDefaultHeader()
                              , _success=self._singupSuccess_
                              , _failed=self._signupFailed_)

    def _singupSuccess_(self, responseData=None):
        print(f'responseData : {responseData}')
        if responseData['result'] == 'OK':
            body = responseData['body']
            AuthenticationManager().add(body['email'], body['token'])

    def _signupFailed_(self, res=None):
        print(f'response status: {res.status_code}')
