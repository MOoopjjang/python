#!python3
# -*- coding:utf -*-


def tst1():
    '''순환체를 언패킹하려는데 요소가 N개 이상 포함되어 "값이 너무 많습니다."라는 예외가 발생한다.'''

    ar = ['a' , 'b' , 'c' , 'd' , 'e']
    a,*middle,e = ar
    print('a : {} , e : {}'.format(a , e))
    print('middle : {}'.format(middle))

    print('-'*30)
    record = ('Dave' , 'aaa@bbb.com' , '1112223333','44455556666')
    name , email , *ph = record
    print('name : {} , email : {}'.format(name , email))
    print('phone: {}'.format(ph))


if __name__ =='__main__':
    tst1()