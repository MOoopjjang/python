#!python
#-*- coding:utf-8 -*-



import socket


def createSrv():

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 8080
	s.bind((host , port))
	s.listen(5)

	while True:
		print('Wating....')
		c , addr = s.accept()
		print('Got connection from {}'.format(addr))
		c.send('Thank for Connection...'.encode())
		c.close()


def main():
	createSrv()



if __name__ == '__main__':
	main()