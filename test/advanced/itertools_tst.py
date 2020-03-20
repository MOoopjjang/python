#!python3
#-*- coding:utf-8 -*-


def chain_tst():
    '''
    chain : 서로다른 container에 들어있으나 , 중첩된 반복문을 사용하지 않고 나열하고 싶다.
    '''
    from itertools import chain

    l1 = [1,2,3]
    l2 = ['a','b','c','d']

    for x in chain(l1 , l2):
        print('x : {}'.format(x))



def cycle_tst():
    '''
    cycle : Iterable한 객체를 넘겨주면 무한히 반보고디는 iterator를 반환한다.
    '''

    def gen_digit(x):
        from itertools import cycle
        from collections import Iterable

        for xx in cycle(x):
            if isinstance( xx , Iterable):
                yield from xx
            else:
                yield xx

    ite = [1,2 ,[3,4],5]
    for x in gen_digit(ite):
        print('x : {}'.format(x))
    



if __name__ == "__main__":
    # cycle_tst()

    chain_tst()









