#!python3


from abc import ABCMeta , abstractmethod


'''
domain class들의 parent class
'''

class BaseDomain(metaclass = ABCMeta):
    def toJSON(self):
        '''
        class의 instance 변수들을 json string 타입으로 반환
        '''
        import json
        return json.dumps(self.__dict__)
