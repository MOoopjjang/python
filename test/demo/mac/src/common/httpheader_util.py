#!python3


'''

'''

def getDefaultHeader():
    '''
    MOoopApi 서버와 연동시 기본 header값 설정
    '''
    return {
        "X-TOKEN-VALUE": "mooop1234"
        , "Content-Type": "application/json"
    }


def getAuthHederInfo(_email , _token , _refreshToken , _gtype = 'bearer'):

    '''
    MOoopApi 서버와 연동시 접근권한이 필요한 resource접근시 적용 header
    '''
    return {
       'X-TOKEN-VALUE' : 'mooop1234'
        ,'Content-Type' : 'application/json'
        ,'grant_type' : _gtype
        ,'X-USER-NAME' : _email
        ,'X-REFRESH-TOKEN' : _refreshToken
        ,'X-AUTH-TOKEN' : _token
    }
