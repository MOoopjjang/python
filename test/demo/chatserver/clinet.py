#!python3
#-*- coding:utf-8 -*-


import socket
import threading


SERVER_INFO = ('0.0.0.0' , 5000)


def recvfunc(csock):
	while True:
		msg = csock.recv(1024)
		print('msg : {}'.format(msg.decode()))


def main():
	csock = socket.socket()
	csock.connect(SERVER_INFO)

	t = threading.Thread(target = recvfunc , args = (csock,))
	t.start()


	while True:
		input_text = input('input :')
		csock.sendall(input_text.encode())
		

	t.join()



if __name__ == '__main__':
	main()