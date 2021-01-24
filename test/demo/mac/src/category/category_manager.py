#!python3
#-*- coding:utf-8 -*-

import src.common.httpheader_util as hutil
from src.common.network_manager import NetworkManager
from src.common.authentication_manager import AuthenticationManager
from src.common.singleton_decorator import SingletonDecorator
from src.category.domain.category_request import CategoryRequest
from pprint import pprint

@SingletonDecorator(tag = "[CM]" , dp = True)
class CategoryManager:
    URI_BASE = 'http://localhost:8080/api/v1/category'
    URI_REG = ''.join([URI_BASE , '/registry'])
    URI_INFO = ''.join([URI_BASE , '/info'])
    URI_LIST = ''.join([URI_BASE , '/list'])
    def __init__(self):pass

    def list(self , _email):
        authInfo = AuthenticationManager().get(_email)
        NetworkManager().get(self.URI_LIST
                             ,hutil.getAuthHederInfo(_email , authInfo.getToken() , authInfo.getRefreshToken())
                             , self._success_
                             , self._fail_
                             )


    def registry(self , _email , _name , _cd):
        authInfo = AuthenticationManager().get(_email)
        cr = CategoryRequest(_name , _cd)
        NetworkManager().post(self.URI_REG
                              ,cr.toJSON()
                              ,hutil.getAuthHederInfo(_email,authInfo.getToken() , authInfo.getRefreshToken())
                              ,self._success_
                              ,self._fail_
                              )

    def info(self , _email , _id):
        authInfo = AuthenticationManager().get(_email)
        infoUrl = ''.join([self.URI_INFO , f'/{_id}'])
        NetworkManager().get(infoUrl
                             ,hutil.getAuthHederInfo(_email , authInfo.getToken() , authInfo.getRefreshToken())
                             , self._success_
                             , self._fail_
                             )

    def _success_(self , responseData):
        pprint(f'success : {responseData}')

    def _fail_(self , response):
        print('error')





    def menu(self , _email):
        while True:
            print('*' * 20)
            print('1. list')
            print('2. registry')
            print('3. info ')
            print('*' * 20)

            inputNumber = input('select:')
            if inputNumber == '1':
                self.list(_email)
            elif inputNumber == '2':
                inputName = input('name : ')
                inputCd = input('cd : ')
                self.registry(_email, inputName, inputCd)
            elif inputNumber == '3':
                inputId = input('ID : ')
                self.info(_email , inputId)
            else:
                break









