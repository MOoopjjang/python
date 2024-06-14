#!python3

from concurrent.futures import ThreadPoolExecutor


def apiCall(_url, _body):
    import requests
    import json

    jsonstr = json.dumps(_body)
    return requests.post(url=_url, headers={"Content-Type": "application/json"}, data=jsonstr)


if __name__ == '__main__':
    URL = "http://localhost:8081/morder/test/auth/signin"

    body = {
        "userId": "cwkim",
        "password": "1111"
    }

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(apiCall, URL, body) for _ in range(48)]
        for future in futures:
            print(f'future = {future.result()}')
