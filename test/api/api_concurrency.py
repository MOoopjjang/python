#!python3
from pprint import pprint

import requests
import json
from concurrent.futures import ProcessPoolExecutor

LOGIN_URL = 'http://localhost:8080/api/auth/login'
PERSONS_LIST = 'http://localhost:8080/api/persons'
PERSONS_COMPLEX = 'http://localhost:8080/api/persons/complex'

EVENT_APPLY_URL = 'http://localhost:8080/event/ticket/apply'


TMP_URL = "http://localhost:8080/test/t1"


class ApiServer:
    def __init__(self, _url):
        self._url_ = _url

    def get(self, _headers=None):
        if _headers is None:
            _headers = {}
        _headers.setdefault('Content-Type', 'application/json')
        _headers.setdefault('Access', 'application/json')
        res = requests.get(self._url_, headers=_headers)
        print(f'status : {res.status_code}')
        return self._result_(res)

    def post(self, _headers=None, _body=None):
        res = None
        if _body is None:
            res = requests.post(self._url_)
        else:
            if _headers is None:
                _headers = {}
            _headers.setdefault('Content-Type', 'application/json')
            _headers.setdefault('Access', 'application/json')
            res = requests.post(self._url_, data=_body, headers=_headers)

        return self._result_(res)

    def _result_(self, _res):
        if _res.status_code == 200:
            return {
                'status': _res.status_code
                , 'result': _res.content
            }
        else:
            return {
                'status': _res.status_code
                , 'result': None
            }


def callApi(_url, _method, _header, _body):
    apiServer = ApiServer(_url)
    if _method == 'GET':
        return apiServer.get(_header)
    else:
        return apiServer.post(_body=_body)


def login():
    jsonString = json.dumps({
        "username": "김철우"
        , "password": "11111"
    })
    return callApi(LOGIN_URL, 'POST', None, jsonString)


def personlist(_token):
    header = {
        "x-access-token": _token
    }
    return callApi(PERSONS_LIST, 'GET', header, None)


def personComplex():
    # header = {
    #     "x-access-token": _token
    # }
    jsonString = json.dumps({
        "id": "c8f82810-db5a-4562-a8e3-21700b3084c4",
        "name": "김병현",
        "age": 11,
        "addr": "용인",
        "job": "프로그래머"
    })
    return callApi(PERSONS_COMPLEX, 'POST', None, jsonString)



def parallel(_apiFunc, _cnt, *args):
    with ProcessPoolExecutor(max_workers=_cnt + 1) as executor:
        futures = [executor.submit(_apiFunc, *args) for _ in range(_cnt)]
        for future in futures:
            r = future.result()
            pprint(json.loads(r['result']))
            # jsonObject = json.loads(r)
            # pprint(jsonObject)



def apiTest():
    response = login()
    if response['status'] == 200:
        r = json.loads(response["result"])
        if r["code"] == "0000":
            accessToken = r["body"]["accessToken"]
            parallel(personComplex, 2, accessToken)
        else:
            print(f'message = {r["message"]}')
    else:
        print(f'result = {response["status"]}')

def t1():
    return callApi(TMP_URL , 'GET' , None , None)

def t2():
    return callApi('http://localhost:8080/functional/test/t1?name=xferlog','GET',None , None)


def t3():
    b = {
        "ticketName":"ticket-1"
    }
    return callApi(EVENT_APPLY_URL , 'POST', None, json.dumps(b))



if __name__ == '__main__':
    # apiTest()
    # parallel(t1, 2)
    # parallel(t2, 2)

    # parallel(personComplex, 2 )

    parallel(t3 , 2)
