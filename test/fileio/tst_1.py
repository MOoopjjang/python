#!python3
# -*- coding:utf-8 -*-

DEFAULT_PATH = '/Users/gimcheol-u/Documents/work/git/python/test/data/'


import os

def getList(_dir):
    if os.path.isdir(_dir):
        print('-' * 20)
        ld = os.listdir(_dir)
        for fname in ld:
            print(f'{fname}')
        print('-'*20)


def t3():
    # 심볼릭링크인지 확인
    getList(DEFAULT_PATH)
    fullPath = ''.join([DEFAULT_PATH , 'xferlog.txt'])
    print(f'심볼릭링크?{os.path.islink(fullPath)}')
    print(f'연결된파일 경로?{os.path.realpath(fullPath)}')





def t2():
    getList(DEFAULT_PATH)
    fullPath = ''.join([DEFAULT_PATH , 'xferlog.txt'])
    print(f'파일존재? {os.path.exists(fullPath)}')
    print(f'디렉토리? : {os.path.isdir(fullPath)}')
    print(f'디렉토리? : {os.path.isdir(os.path.dirname(fullPath))}')
    print(f'파일?: {os.path.isfile(fullPath)}')




def t1():
    getList(DEFAULT_PATH)

    fullPath = ''.join([DEFAULT_PATH , 'xferlog.txt'])
    print(f'fullPath : {fullPath }')
    print(f'filename : {os.path.basename(fullPath)}')
    print(f'dirname : {os.path.dirname(fullPath)}')
    print(f'경로합치기 : {os.path.join("tmp" , "data" , os.path.basename(fullPath))}')
    print(f'파일확장자 분리: {os.path.splitext(fullPath)}')

def read_txt():
    getList(DEFAULT_PATH)
    fullPath = ''.join([DEFAULT_PATH, 'sample.txt'])

    with open(fullPath , 'rt' , encoding='utf-8') as fr:
        for line in fr:
            print(f'line : {line}' , end='')


def write_txt():
    t ='''
i'am hello
kadklklfalkfla
1111111
'''

    fulUrl = os.path.join(DEFAULT_PATH , 'defffff.txt')
    with open(fulUrl , 'wt' , newline='') as fw:
        fw.write(t)


    t = 'append'
    with open(fulUrl , 'at') as aw:
        aw.write(t)




if __name__ == '__main__':
    # t1()
    # t2()
    # t3()
    read_txt()
    # write_txt()
