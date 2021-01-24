#!python3
# -*- coding:utf-8 -*-

from src.common.authentication_manager import AuthenticationManager
from src.signin.sign_manager import SignManager
from src.category.category_manager import CategoryManager
from src.mfile.mfile_manager import MFileManager


menuDict = {
    "1":SignManager().menu
    ,"2":CategoryManager().menu
    ,"3":MFileManager().menu
}


def main():
    while True:
        print('*'*20)
        print('1. signin')
        print('2. category')
        print('3. file')
        print('4. exit ')
        print('*'*20)
        inputNum = input('select:')
        if inputNum not in ["1" , "2" , "3"]:break

        if inputNum == '1':
            menuDict[inputNum]()
        else:
            inputEmail = input('select email:')
            menuDict[inputNum](inputEmail)





if __name__ == '__main__':
    main()