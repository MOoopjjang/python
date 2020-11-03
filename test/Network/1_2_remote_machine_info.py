#!python3
# -*- coding:utf-8 -*-


import socket


def find_service_name():
    '''
     - port번호와 protocol이름으로 서비스이름찾기
    '''
    protocolname = 'tcp'
    for port in [80 , 22]:
        print('Port : {} => service name : {}'.format(port , socket.getservbyport(port , protocolname)))


def convert_ip4_address():
    from binascii import hexlify
    for ip_addr in ['127.0.0.1' , '192.168.0,1']:
        packed_ip_addr = socket.inet_aton(ip_addr)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print('IP Address : {} => Packed: {} , Unpacked : {}'.format(ip_addr , hexlify(packed_ip_addr ), unpacked_ip_addr))


def tst1():
    '''
     - host ( www.python.org)에 해당되는 IP 출력
    '''
    remote_host = 'www.python.org'
    try:
        print('IP address of {} : {}'.format(socket.gethostbyname(remote_host),remote_host))
    except socket.error as err_msg:
        print(f'{remote_host} - {err_msg}')


if __name__ == '__main__':
    # tst1()
    # convert_ip4_address()
    find_service_name()
