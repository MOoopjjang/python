#!python3
# -*- coding:utf-8 -*-

'''
 - 이분 검색 테스트
 - 코드 refactoring 필요
'''

DIVIDE = 2


def bsearch(_ar, v, _cnt):
    _cnt += 1

    print(f'count >>{_cnt}')
    print(f'_ar : {_ar}')

    size = len(_ar)
    m = int(size / 2) - 1
    if m < 0: m = 0

    if _ar[m] == v:
        print(f'find m : {_ar[m]}')
    else:
        if _ar[m] < v:
            bsearch(_ar[m + 1:], v, _cnt)
        else:
            bsearch(_ar[:m], v, _cnt)


def bsearch2(_ar , v , _cnt):
    l = 0
    r = ( l + _cnt)-1
    while l <= r:
        m =  int(( l + r )/2)

        print(f'>>> m = {m}')
        if v == _ar[m]:
            return m

        if v < _ar[m]:
            r = m-1
        else:
            l = m+1

    return None



if __name__ == '__main__':
    iv = int(input('v :'))

    ar = [i for i in range(20)]
    # bsearch(ar, iv, 0)
    result = bsearch2(ar, iv, len(ar))
    print(f'result = {result}')
