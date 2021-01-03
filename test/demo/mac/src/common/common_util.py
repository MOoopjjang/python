#!python3
# -*- coding:utf-8 -*-


def getMemberInfo(mlist, _dict):
    '''
    인스턴스 멤버들의 정보를 반환한다.
    '''

    def getType(_v):
        primitiveTypes = [str, int, list, tuple, set]
        primitive2Types = [dict]

        l = [filter(lambda x: isinstance(_v, x) == True, primitiveTypes)]
        if len(l) > 0:
            return "1"
        elif isinstance(_v, dict):
            return "2"
        else:
            return "3"

    for k, v in _dict.items():
        print(f'k ::: {k} : {v}')
        type = getType(v)
        print(f'type : {type}')
        if type == "2":
            getMemberInfo(mlist, v)
        elif type == "3":
            getMemberInfo(mlist, v.__dict__)
        mlist.append(f'{k}:{v}')

    # l = [ f'{k}:{v}' for k,v in _instance.__dict__.items() ]
    # return f'{_delimiter}'.join(l)


def getDefaultHeader():
    '''
    MOoopApi 서버와 연동시 기본 header값 설정
    '''
    return {
        "X-TOKEN-VALUE": "mooop1234"
        , "Content-Type": "application/json"
    }


def getAuthHederInfo(_authInfo): pass
