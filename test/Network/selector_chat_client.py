#!python3
#-*- coding:utf-8 -*-


import socket


HOST = '127.0.0.1'
PORT = 5000


if __name__ == '__main__':
	srv_sock = socket.socket()
	srv_sock.connect((HOST , PORT))

	while True:
		input_msg = input('>>')
		srv_sock.sendall(input_msg.encode())

		recv_msg = srv_sock.recv(1024)
		print('recv :{}'.format(recv_msg.decode()))


