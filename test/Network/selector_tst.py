#!python3
#-*- coding:utf-8 -*-

"""
Selector를 사용한 소켓 멀티플렉싱 ( echo server )
"""


import selectors
import socket



def read_sock(cli_sock , mask ):
	msg = cli_sock.recv(1024)
	if msg:
		print('rcv : {}'.format(msg.decode()))
		cli_sock.sendall(msg)
	else:
		sel.unregister(cli_sock)
		cli_sock.close()


def accept_handler(serv_sock , mask):
	cli_sock , cli_addr = serv_sock.accept()
	print('accept {}'.format(cli_addr))
	cli_sock.setblocking(False)
	sel.register(cli_sock , selectors.EVENT_READ , read_sock)



sel = selectors.DefaultSelector()
sock = socket.socket()
sock.bind(('0.0.0.0' , 5000))
sock.listen(100)
sock.setblocking(False)

sel.register(sock , selectors.EVENT_READ , accept_handler)


if __name__ == '__main__':
	while True:
		events = sel.select()
		for key , mask in events:
			callback = key.data
			callback(key.fileobj , mask)

