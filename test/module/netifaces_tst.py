#!python3
#-*- coding:utf-8 -*-



import netifaces as ni
import uuid


"""
  NetworkInfaceCard에 대한 정보를 제공하는 module
   ( netmask , NIC Name , mad_address ...)

  Reference :
	  https://pypi.org/project/netifaces/ 
"""


def getNIC(mac_address):
	nic = 'unknown'
	for card in ni.interfaces():
		addrs = ni.ifaddresses(card)
		if bool(addrs) and ni.AF_LINK in addrs:
			for member in addrs[ni.AF_LINK]:
				if 'addr' in member  and member['addr'] == mac_address:
					nic = card
					break
			if nic != 'unknown':break


	return nic


def tst_1():


	mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

	nic = getNIC(mac_address)
	print('nic : {}'.format(nic))




if __name__ == '__main__':
	tst_1()