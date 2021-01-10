#!python3

from src.common.network_manager import NetworkManager
from src.common.authentication_manager import AuthenticationManager
from src.common.singleton_decorator import SingletonDecorator
from src.mfile.domain.mfile_search_request import MFileSearchRequest
import src.common.httpheader_util as hutil


@SingletonDecorator(tag="MFM", dp=True)
class MFileManager:
    BASE_URI = 'http://localhost:8080/api/v1/file'
    LIST_URI = ''.join([BASE_URI , "/list?from=0&size=10"])
    SEARCH_URI = ''.join([BASE_URI , '/search'])

    def getList(self, _email):
        authInfo = AuthenticationManager().get(_email)
        NetworkManager().get(self.LIST_URI
                             ,headers = hutil.getAuthHederInfo(authInfo.getEmail() , authInfo.getToken() , authInfo.getRefreshToken())
                             ,_success= self._successFunc_
                             ,_failed= self._failedFunc_)

    def search(self , _email , _searchType , _value , _page = 0 , _size = 10):
        authInfo = AuthenticationManager().get(_email)
        r = MFileSearchRequest(_searchType , _value , _page , _size)
        NetworkManager().post(self.SEARCH_URI
                              ,data = r.toJSON()
                              ,headers = hutil.getAuthHederInfo(authInfo.getEmail() , authInfo.getToken() , authInfo.getRefreshToken())
                              , _success=self._successFunc_
                              , _failed=self._failedFunc_)





    def _successFunc_(self , responseData):
        print(f'{responseData}')


    def _failedFunc_(self , res):
        print('failed')
