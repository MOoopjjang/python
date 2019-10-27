#!python3
#-*- coding:utf-8 -*-


import socket


if __name__ == '__main__':
	socket = socket.socket()
	socket.connect(('127.0.0.1' , 5000))

	socket.send('hi'.encode())

	msg = socket.recv(1024)
	print('recv : {}'.format(msg.decode()))

	socket.close()