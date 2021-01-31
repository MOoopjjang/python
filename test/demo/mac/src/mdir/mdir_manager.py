#!python3
# -*- coding:utf-8 -*-


from src.common.authentication_manager import AuthenticationManager
from src.mdir.domain.mdir_registry_request import MDirRegistryRequest
from src.common.network_manager import NetworkManager
import src.common.httpheader_util as hutil


class MDirManager:
    URI_BASE = 'http://localhost:8080/api/v1/mdir'
    URI_REGISTRY = ''.join([URI_BASE , '/registry'])

    def menu(self , _email):
        while True:
            print('*'*20)
            print('1 . registry')
            print('u , up menu ')
            print('*'*20)
            inputNum = input('select: ')
            if inputNum == '1':
                inputName = input('input name :')
                inputPath = input('input path :')
                self.registry(_email , inputName , inputPath)



    def registry(self , _email , _name , _path):
        authInfo = AuthenticationManager().get(_email)

        data = MDirRegistryRequest(_name , _path)
        NetworkManager().post(self.URI_REGISTRY
                              ,data = data.toJSON()
                              ,headers = hutil.getAuthHederInfo( _email , authInfo.getToken() , authInfo.getRefreshToken())
                              ,_success=self._success_
                              ,_failed=self._failed_
                              )


    def _success_(self , reesponseData):
        print(f'responseData : {reesponseData}')


    def _failed_(self , response ):
        print('error')




