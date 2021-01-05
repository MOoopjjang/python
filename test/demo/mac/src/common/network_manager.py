#!python3
# -*- coding:utf-8 -*-

from src.common.singleton_decorator import SingletonDecorator
import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError
from requests.packages.urllib3.util.retry import Retry


@SingletonDecorator(tag="[NM]", dp=True)
class NetworkManager:
    def post(self, uri=None, data=None, headers=None, _success=None, _failed=None):
        '''

        '''
        try:
            session = self._retry_session_()
            res = session.post(uri, data=data, headers=headers)
            if res.status_code == 200:
                _success(res.json())
            else:
                _failed(res)
        except ConnectionError as ce:
            print(ce)

    def get(self, uri=None, headers=None, _success=None, _failed=None):
        '''

        '''
        try:
            session = self._retry_session_()
            res = session.get(url=uri, headers=headers)
            if res.status_code == 200:
                _success(res.json())
            else:
                _failed(res)
        except ConnectionError as ce:
            print(ce)

    def _retry_session_(self):
        session = requests.session()
        retry = Retry(
            total=3,
            read=3,
            backoff_factor=0.3,
            status_forcelist=(500, 400),
            method_whitelist=('GET', 'POST')
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session
