#!python3.7.3
# -*- coding:utf-8 -*-


def test1():
    import requests
    from pprint import pprint

    res = requests.get('http://localhost:8080/mtw/test/sample/json')
    if res.status_code == 200:
        pprint(res.json())
        d = dict(res.json())
        print('d : {}'.format(d))


if __name__ == '__main__':
    test1()
