#!python3
# -*- coding:utf-8 -*-


'''
 - Queue에 저장될 class
 - MThread에서 수행될 작업 class
'''


class MPool:
    def __init__(self, eFunc=None, eData=None):
        if eFunc == None or eData == None:
            raise Exception("parameter error == null")

        self.eFunc = eFunc
        self.eData = eData
