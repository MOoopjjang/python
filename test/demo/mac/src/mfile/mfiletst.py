#!python3
# -*- coding:utf-8 -*-


from src.signin.sign_manager import SignManager
from src.mfile.mfile_manager import MFileManager


def list_tst():
    SignManager().signup("aaa@bbb.com","1111" , "xferlog")


    while True:
        print('*'*20)
        print('1 . list ')
        print('2 . search ')
        print('3 . info ')
        inputNumber = input('select:')

        if inputNumber == '1':
            MFileManager().getList('aaa@bbb.com')
        elif inputNumber == '2':
            inputType = input('type:')
            inputValue = input('value:')
            MFileManager().search("aaa@bbb.com" , inputType , inputValue)
        elif inputNumber == '3':
            inputid = input('id:')
            MFileManager().getInfo('aaa@bbb.com' , inputid)
        else:
            break



if __name__ == '__main__':
    list_tst()
