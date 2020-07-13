#!python3
# -*- coding:utf-8 -*-


def tst1():
    import timeit

    ar = [1,23,45,11,89,3,4,65,22,31]
    print('len : {}'.format(len(ar)))

    s = timeit.default_timer()


if __name__ == '__main__':
    tst1()