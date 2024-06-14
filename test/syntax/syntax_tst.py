#!/bin/python


def range_tst(_s):
    print(f'_s = {_s}')
    for i in range(0 , len(_s),2):
        print(f'{_s[i]}')




def t1():
    input_number = int(input("input number:"))
    print(f'{type(input_number) }')
    if type(input_number) is int:
        print('input_number type int')


if __name__ == '__main__':
    # t1()
    range_tst('xferlog')
