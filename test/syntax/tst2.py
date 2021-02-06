#!python3
#-*- coding:utf-8 -*-



def tst1():
    print('tst1')


    def args_tst(name , age = None ,  *args):
        print(f'type:{type(args)} , len:{len(args)}')
        print(f'name : {name}')
        print(f'args : {args}')
        for i,v in enumerate( args ):
            print(f'{i} : {v}')

    args_tst('kim', 10,'xferlog' , 'kknda')
    args_tst('xferlog',1)

    print('*'*20)

    def kargw_tst(name = None , age = None , **kwargs):
        print(f'name : {name} , age : {age}')
        for k,v in kwargs.items():
            print(f'{k}:{v}')

    kargw_tst('kim' , 0 , price=20 , value=20)
    kargw_tst( price=20 , value=20)


if __name__ == '__main__':
    tst1()
