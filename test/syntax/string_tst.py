#!python3
#-*- coding:utf-8 -*-




"""
string 테스트
"""



SAMPLE_1 = 'xferlog kknda iablc iadifladkfalkflkak123 : '




def tst1():
    print('-'*20)
    print(f'SAMLPLE_1{SAMPLE_1}')
    print('-'*20)
    f = SAMPLE_1.find("ia")
    print(f'find {f}')
    print('------------ reverse ------------')
    print(f'{SAMPLE_1[::-1]}')
    print('------------ startswith ------------')
    print(f'start \"xferlog\" ==> {SAMPLE_1.startswith("xferlog")}')
    print(f'start \"kknda\" ==> {SAMPLE_1.startswith("kknda")}')
    print('------------ endswith ------------')
    print(f'123 end ==> {SAMPLE_1.endswith("123 :")}')
    print('------------ strip() ------------')
    print(f'before len : {len(SAMPLE_1)}')
    stripStr = SAMPLE_1.strip(' ')
    print(f' {stripStr}')
    print(f'after len : {len(stripStr)}')
    print('------------ splic ------------')
    print(f'{SAMPLE_1[2:5]}')
    print('------------ join ------------')
    ll = ['xferog','kknda','ccc','ddd']
    joinLL = ','.join(ll)
    print(f'{joinLL}')
    lll = joinLL.split(",")
    print(f'{lll}')




if __name__ == '__main__':
	tst1()
