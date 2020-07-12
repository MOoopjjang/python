#!python3
# -*- coding:utf-8 -*-

COUNT = 0

LEFT = []
MID = []
RIGHT = []


'''
 하노이의 탑
 - 3개의 기둥 ( array [ left , middle , right ] )필요
 순서 :
  1. v = l pop
  2.  
     if len(r) == 0 r.push
     elif len(m) == 0 m.push
  3. r 값 조절
     if len(r) > 0 r.pop
     m.push(v)
     
'''
def hanoi_tst1( l , m , r):
    if len(l) == 0:
        print('='*20)
        return
    else:
        print('{} - {} - {}'.format(l , m , r))
        v = l.pop(0)



def recursive_tst1( count  , max):
    if max == count:
        return
    else:
        count +=1
        print('count : {} , max : {}'.format(count , max))
        recursive_tst1( count , max)


def test(_ar):
    if len(_ar) == 0:
        return
    else:
        v = _ar.pop(0)
        print('v : {}'.format(v))
        test(_ar)

MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"


def move(N, start, to):
    print(MSG_FORMAT.format(N, start, to))

def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)
if __name__ == '__main__':
#    l , m , r= [1,2,3,4,5] ,[] , []
#    hanoiOfTown_tst1(l , m , r)

    hanoi(5 , 'A' , 'C' , 'B')





