#!python3
# -*- coding:utf -*-


"""
 - Queue에 저장될 작업객체
"""

class MQueueObj:
    def __init__(self , eFunc = None , eData = None):
        if eFunc == None or eData == None:
            raise Exception("parameter is None ")

        self.eFunc = eFunc
        self.eData = eData