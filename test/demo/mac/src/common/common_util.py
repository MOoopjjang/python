#!python3
# -*- coding:utf-8 -*-


def getInstanceMemberInfo(mlist, _d):
    '''
    인스턴스 멤버들의 정보를 반환한다.
    '''

    def getType(_v):
        primitiveTypes = [str, int, list, tuple, set]
        if isinstance(_v , dict):
            return "2"
        else:
            for t in primitiveTypes:
                if isinstance(_v , t):
                    return "1"
            return "3"

    for k, v in _d.items():
        type = getType(v)
        if type == "2":
            getInstanceMemberInfo(mlist, v)
        elif type == "3":
            getInstanceMemberInfo(mlist, v.__dict__)
        mlist.append(f'{k}:{v}')


