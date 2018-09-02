#!python
#-*- coding:utf-8 -*-


import socket
import logging

def init():
	logging.basicConfig(level = logging.DEBUG , format = ' %(asctime)s - %(levelname)s - %(message)s')

def createCli():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 8080

	# logging.debug(help(s))
	s.connect((host , port))
	print('rcv : {}'.format(s.recv(1024).decode()))
	s.close()


def main():
	init()
	createCli()


if __name__ == '__main__':
	main()