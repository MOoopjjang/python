#!python3
# -*- coding:utf-8 -*-


import requests , json


URI = "http://localhost:8080"

authentication = {
    "email":"aaaa@bbb.com",
    "password":"cwkim123",
    "username":"kcwda"
}

header = {
    "Content-Type":"application/json"
}



menuMap = {}

def signup():
    fUrl = URI+"/api/v1/users"
    try:
        res = requests.post(fUrl , data = json.dumps(authentication) , headers = header)
        if res.status_code == 200:
            print(f'response : {res.json()}')
        else:
            print(f'status : {res.status_code}')
    except Exception as e:
        print(f'exception : {e}')




def signin():
    fUri = URI+"/api/v1/signin"
    try:
        res = requests.post(fUri , data = json.dumps(authentication) , headers = header)
        if res.status_code == 200:
            print('token:')
            print(f'{res.json()}')
        else:
            print(f'error : {res.status_code}')
    except Exception as e:
        print(f'e : {e}')




def init():
    global menuMap

    menuMap['signup'] = signup
    menuMap['signin'] = signin






def main():
    init()
    while True:
        for  index , key in enumerate(menuMap.keys()):
            print(f'{index} . {key} ')

        inputkey = input('select key : ')
        if inputkey == '':break

        menuMap[inputkey]()



if __name__ == '__main__':
    main()