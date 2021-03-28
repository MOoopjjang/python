#!python3
# -*- coding:utf-8 -*-

'''
 - 이진 검색 테스트
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


if __name__ == '__main__':
    iv = int(input('v :'))

    ar = [i for i in range(100000)]
    bsearch(ar, iv, 0)
