#!python3
# -*- coding:utf-8 -*-


from kafka import KafkaProducer
from json import dumps
import time

'''

url : https://m.blog.naver.com/wideeyed/221973877361

'''


def on_send_success(metadata):
    #보낸 데이터의 metadata를 출력한다.
    print(f'{metadata}')


if __name__ == '__main__':
    # 카프카 서버
    bootstrap_servers = ["localhost:9092"]

    #카프카 공급자 생성
    producer = KafkaProducer(
        bootstrap_servers = bootstrap_servers,
        key_serializer = None,
        value_serializer = lambda x: dumps(x).encode('utf-8')
    )
    # kafka 토픽
    str_topic_name = 'Topic1'

    data = {'time' : time.time()}
    producer.send(str_topic_name , value=data).add_callback(on_send_success).get(timeout=100)

    print(f'data : {data}')

