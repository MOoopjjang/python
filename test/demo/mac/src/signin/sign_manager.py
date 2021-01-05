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
    BASE_URL = "http://localhost:8080"
    SIGNIN_URI = ''.join([BASE_URL, '/api/v1/user/registry'])
    LOGIN_URI = ''.join([BASE_URL , '/api/v1/user/login'])
    REFRESH_URI = ''.join([BASE_URL, '/api/v1/user/refresh'])

    def signup(self, email, password, username):
        userRequest = UserRequest(email, password, username)
        NetworkManager().post(self.SIGNIN_URI
                              , data=userRequest.toJSON()
                              , headers=hhutil.getDefaultHeader()
                              , _success=self._singupSuccess_
                              , _failed=self._signupFailed_)


    def login(self , _email , _password):
        userRequest = UserRequest(_email , _password , "")
        NetworkManager().post(self.LOGIN_URI
                              ,data = userRequest.toJSON()
                              ,headers = hhutil.getDefaultHeader()
                              ,_success = self._singupSuccess_
                              ,_failed=self._signupFailed_
                              )



    def refresh(self , _email):
        authInfo = AuthenticationManager().get(_email)
        NetworkManager().get(self.REFRESH_URI
                            ,headers = hhutil.getAuthHederInfo(authInfo.getEmail() , authInfo.getToken() , authInfo.getRefreshToken())
                            ,_success = self._refreshSuccess_
                            ,_failed = self._refreshFailed_
                             )






    def _singupSuccess_(self, responseData=None):
        print(f'responseData : {responseData}')
        if responseData['result'] == 'OK':
            body = responseData['body']
            AuthenticationManager().add(body['email'], body['token'] , body['refreshToken'])

    def _signupFailed_(self, res=None):
        print(f'response status: {res.status_code}')



    def _refreshSuccess_(self , responseData = None):
        print(f'responseData : {responseData}')
        if responseData['result'] == 'OK':
            body = responseData['body']
            authInfo = AuthenticationManager().get(body['email'])
            print(f'{authInfo.getRefreshToken()} ---> {body["token"]}')
            AuthenticationManager().add(body['email'], body['token'] , body['refreshToken'])

    def _refreshFailed_(self , res = None):
        print(f'response status: {res.status_code}')
