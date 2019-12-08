#!python3
#-*- coding:utf-8 -*-


import socket


SERVER_INFO = ('0.0.0.0' , 5000)

def main():
	csock = socket.socket()
	csock.connect(SERVER_INFO)

	while True:
		input_text = input('input :')

		csock.sendall(input_text.encode())
		msg = csock.recv(1024)
		print('msg : {}'.format(msg.decode()))




if __name__ == '__main__':
	main()