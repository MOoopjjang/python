#!python
#-*- coding:utf-8 -*-



def tst2():
    ar = ["xferlog" , "kknda" , "aaa"]

    if "xferlog" in ar:print("exist")


def tst3():
    ar = ['dlh1' , 'dlg2']
    sAr = sorted(ar , reverse=False)
    print(f'sAr : {sAr}')

    print(f'=== {"dlg1" < "dlg2"}')



def test():
    ''' loop 안에 multi 조건연산자 '''
    v = [i for i in range(1,100) if i>10 if i%2 == 0]
    print('v : {}'.format(v))




if __name__ == '__main__':
    # test()
    # tst2()
    tst3()


