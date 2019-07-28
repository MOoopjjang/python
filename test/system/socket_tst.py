#!python3
#-*- coding:utf-8 -*-



"""
  sokcet module 테스트
"""

import socket




def tst_1():
	"""
	도메인 이름에 대한 IP 정보 확인하기
	"""

	host = socket.gethostbyname_ex('www.google.com')
	print('\n'+'-'*10+'host 정보를 출력'+'-'*10)
	print(host)

	print('\n'+'-'*10+'for문을 이용하여 한줄씩 출력'+'-'*10)
	for h in host:print(h)

	print('\n'+'-'*10+'IP 주소 선택'+'-'*10)
	hostname , aliaslist , ipaddrlist = host
	print(ipaddrlist[0])




if __name__ == '__main__':
	tst_1()
