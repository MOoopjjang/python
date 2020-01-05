#!python3
#-*- coding:utf-8 -*-


import socket
import threading


SERVER_INFO = ('0.0.0.0' , 5000)


def recvfunc(csock):
	while True:
		msg = csock.recv(1024)
		print('\nmsg : {}'.format(msg.decode()) , end='')
		if msg == None or len(msg) == 0:
			break


def main():
	csock = socket.socket()
	csock.connect(SERVER_INFO)

	t = threading.Thread(target = recvfunc , args = (csock,))
	t.start()


	while True:
		input_text = input()
		csock.sendall(input_text.encode())
		

	t.join()



if __name__ == '__main__':
	main()