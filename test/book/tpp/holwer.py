#!python3
#-*- coding:utf-8 -*-


#######################################
#
#  파일이나 문자열을 입력받아 영어를 대문자로 변환
#
#######################################

import argparse,os
import re

FILTER = '[a-zA-Z]'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='소문자를 대문자로 변환')
    parser.add_argument('-t' , '--arg1')
    parser.add_argument('-f' , '--arg2')

    args = parser.parse_args()
    if args.arg1 is None or args.arg2 is None:
        print('User -t option text and -f option file')
        exit(1)

    print(f'arg1 = {args.arg1}')
    print(f'arg1 = {args.arg2}')
