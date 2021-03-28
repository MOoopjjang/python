#!python3


from kafka import KafkaConsumer
from json import loads



if __name__ == '__main__':
    bootstrap_server = ['localhost:9092']

    str_topic = 'Topic1'

    #kafka 소비자 group1 생성
    str_group_name = 'group1'
    consumer = KafkaConsumer(str_topic , bootstrap_servers = bootstrap_server,
                             auto_offset_reset='earlist',  #가장 처음부터 소비
                             enable_auto_commit=True,
                             group_id=str_group_name,
                             value_deserializer=lambda x: loads(x.decode('utf-8')),
                             consumer_timeout_ms=60000  #타임아웃 지정
                             )

    for message in consumer:
        print(f'{message}')


