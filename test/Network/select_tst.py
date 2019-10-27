#!python3
#-*- coding:utf-8 -*-



import socket
import select


"""
 멀티플렉싱 ( select 모듈 ) 테스트코드
"""


server_sock = socket.socket()
server_sock.bind(('0.0.0.0' , 5000))
server_sock.listen()


server_sock2 = socket.socket()
server_sock2.bind(('0.0.0.0' , 5001))
server_sock2.listen()

server_socks = [server_sock , server_sock2]



if __name__ == '__main__':

	while True:
		conn_read_socket_list , conn_write_socket_list , conn_except_socket_list = select.select(server_socks , [] , [])

		for rsock in conn_read_socket_list:
			if rsock == server_sock:
				print('server_sock')
				cli_sock , cli_addr = rsock.accept()
				msg = cli_sock.recv(1024)
				print('{} : {}'.format(cli_addr , msg.decoe()))
				cli_sock.sendall('hello 5000'.encode())
				cli_sock.close()
			elif rsock == server_sock2:
				print('server_sock2')
				cli_sock , cli_addr = rsock.accept()
				msg = cli_sock.recv(1024)
				print('{} : {}'.format(cli_addr , msg.decoe()))
				cli_sock.sendall('hello 5000'.encode())
				cli_sock.close()




