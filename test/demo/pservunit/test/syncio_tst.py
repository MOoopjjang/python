#!python3

from concurrent.futures import ProcessPoolExecutor


def call_api(_url):
    import requests
    return requests.get(_url)


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(call_api, 'http://localhost:9080/api/t2') for _ in range(3)]
        for future in futures:
            future.result()
