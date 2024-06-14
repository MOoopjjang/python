#!python3
# -*- coding:utf-8 -*-


import os, sys
import copy

LIST_SAMPLE = ['xferlog', 'kknda', 'kim', 'aee', 'ciek', 'abc', 'ciek']
LIST_SAMPLE2 = ['kim', 'park', 'lee', 'kim', 'kim', 'park']


def test():
    print('*' * 100)
    for  i,v in enumerate( LIST_SAMPLE):
        print(f'i = {i}, v = {v}')

    LIST_TMP1 = LIST_SAMPLE[2::2]
    print(f'LIST_TMP1 = {LIST_TMP1}')
    print('*' * 100)
    LIST_TMP1.append('app1')
    print(f'append LIST_TMP1 = {LIST_TMP1}')
    del LIST_TMP1[len(LIST_TMP1)-1]
    print(f'del LIST_TMP1 = {LIST_TMP1}')
    LIST_TMP1.insert(2 , '22222')
    print(f'insert LIST_TMP1 = {LIST_TMP1}')
    print('*' * 100)
    l = []
    for v in LIST_SAMPLE:
        if v not in l:
            print(f'\'{v}\' count:{LIST_SAMPLE.count(v)}')
            l.append(v)

    print("*"*100)
    l = [i for i in range(10)]
    print(f'{l}')
    print(f'{LIST_SAMPLE.extend( [i for i in range(10)])}')





def test2():
    rlist = LIST_SAMPLE[::-1]
    print(f'LIST_SAMPLE : {LIST_SAMPLE}')
    print(f'rlist : {rlist}')

    LIST_SAMPLE[3] = "ddddd"
    print(f'LIST_SAMPLE : {LIST_SAMPLE}')
    del LIST_SAMPLE[3]
    print(f'LIST_SAMPLE : {LIST_SAMPLE}')


def test3():
    for i in range(10):
        print(f'{i}')

    ll = [i + 10 for i in range(10)]
    print(f'{ll}')


def test4():
    LIST_SAMPLE.sort()
    print(f'sList : {LIST_SAMPLE}')
    LIST_SAMPLE.sort(reverse=True)
    print(f'sList : {LIST_SAMPLE}')
    ssl = sorted(LIST_SAMPLE, reverse=False)
    print(f'ssl : {ssl}')


def exam_cat_name_list():
    l = []
    while True:
        catName = input('Name:')
        if catName == '' or catName == None:
            break
        if catName not in l:
            l.append(catName)
    print(f'{l}')


# def test2():
# 	v = LIST_SAMPLE & LIST_SAMPLE2
# 	print('v : {}'.format(v))


def count_method_tst():
    # count
    while True:
        for sample in LIST_SAMPLE2: print('{}'.format(sample))
        count_str = input('input item :')
        if count_str == 'q': break
        count = LIST_SAMPLE2.count(count_str)
        print(count_str + ' count : {}'.format(count))


def extend_method_tst():
    LIST_SAMPLE.extend(['1', '2', '3'])
    print('LIST_SAMPLE : {}'.format(LIST_SAMPLE))


if __name__ == '__main__':
    test()
    # test2()
    # test3()
    # test4()

# count_method_tst()
#	extend_method_tst()
# cat_exam()
