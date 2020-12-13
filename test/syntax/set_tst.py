#!python3
# -*- coding:utf-8 -*-

SAMPLE_DATA1 = '1,2,3'
SAMPLE_DATA2 = '3,4,5'


def tst2():
   s1 = set()
   s1.add(1)
   print(f's1 : {s1}')
   s1.add(2)
   print(f's1 : {s1}')
   s1.update([2,3])
   print(f's1 : {s1}')
   s1.remove(2)
   print(f's1 : {s1}')


def tst1():
    print(f'SAMPLE_DATA1 : {SAMPLE_DATA1} , SAMPLE_DATA2 : {SAMPLE_DATA2}')
    s1 = set(SAMPLE_DATA1)
    s2 = set(SAMPLE_DATA2)
    print('------------------------------------')
    print(f' 1 contains SAMPLE_DATA1: {"1" in SAMPLE_DATA1.split(",")}')
    print("----------------  합집합 ------------")
    sums = s1 | s2
    print(f'sum : {sums}')
    print('---------------- 차집합 -------------')
    difs = s1 - s2
    print(f'difs : {difs}')
    print('---------------- 교집합 -------------')
    cs = s1 & s2
    print(f'cs : {cs}')
    print('---------------- 대칭차집합 -------------')
    crossdifs = s1^s2
    print(f'crossdifs : {sorted(crossdifs)}')



if __name__ == '__main__':
    # tst1()
     tst2()
