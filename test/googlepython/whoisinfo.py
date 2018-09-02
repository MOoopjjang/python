#!python3
# -*- coding:utf-8 -*-


import json
import csv
import requests
import os , sys
from mooop.utils import mloggingutil as logutil

AUTH_KEY = '2018071609590114800669'
iplist = None
infoList = []


def init():
	logutil.init()


def loadList():
	global iplist
	fr = open(os.getcwd()+'/iplist.txt' , 'r')
	iplist = [line.strip() for line in fr]
	logutil.getLogger().debug('{}'.format(iplist))


def apiSearch():
	global infoList
	
	session = requests.session()
	for l in iplist:
		try:
			info = []
			res = session.get('http://whois.kisa.or.kr/openapi/whois.jsp?query={}&key={}&answer=json'.format(l , AUTH_KEY))
			res.raise_for_status()
			jl = json.loads(res.text)
			info.append(jl.get('whois')['query'])
			kk = 'PI' if 'PI' in jl['whois']['korean'].keys() else 'ISP'
			info.append(jl['whois']['korean'][kk]['netinfo']['addr'])

			infoList.append(info)
		except:
			print('exception!!')
		



def saveCsv():
	fw = open(os.getcwd()+'/whoisinfo.csv' , 'w' , newline = '' , encoding = 'utf-8')
	cw = csv.writer(fw)
	for row in infoList:
		cw.writerow(row)
	fw.close()


def main():
	init()
	loadList()
	apiSearch()
	saveCsv()


if __name__ == '__main__':
	main()