
#-*- coding:utf-8 -*-

import sys
import os
import logging
import requests
import re
import time

	
def init():
	global logger
	logging.basicConfig(level = logging.INFO , format = ' %(asctime)s - %(levelname)s - %(message)s')
	logger = logging.getLogger(__file__)

def setLoggingLevel(_lvl):
	global logger
	logger.setLevel(logging.DEBUG) if _lvl == 'd' else logger.setLevel(logging.INFO) 


def testCsv():
	import csv
	# examfile = open('example.csv' , 'r')
	# reader = csv.reader(examfile);

	# for row in reader:
	# 	logging.debug('{}:{}'.format(reader.line_num , row))



	# writeFile = open('example_w.csv' , 'w' )
	# writer = csv.writer(writeFile, delimiter = '\t' , lineterminator = '\n\n\n')
	# writer.writerow(['xferlog' , 'kknda' , 'kcwda'])
	# writer.writerow(['aaaa' , 'bbbb' , 'cccc' , 'dddd'])
	# writer.writerow([1,2,3,4,5])
	# writeFile.close()	



	flist = os.listdir(os.getcwd())
	for f in flist:
		if f.endswith('.csv'):
			fread = open(f , 'r')
			creader = csv.reader(fread)

			for row in creader:
				logging.debug('{}'.format(creader.line_num))


def testJSON():
	import json
	sam_dic = '{"name":"xferlog","age":20,"job":"programmer","etc":null}'


	jload = json.loads(sam_dic)
	logging.debug('{}'.format(jload))

	js = json.dumps(sam_dic)
	logging.debug('{}'.format(js))



def getSfp():
	fulUrl = 'http://localhost:8080/sfp/user/email/'+sys.argv[1]
	logging.debug('url : {}'.format(fulUrl))

	res = requests.get(fulUrl)
	res.raise_for_status()
	# logging.debug('{}'.format(res.text))

	jdata = json.loads(res.text)
	logging.debug('convert : {}'.format(jdata))
	# logging.debug(help(jdata))
	for keys , v in jdata.items():
		if keys == 'data':
			for vv in v:
				print('id:{} , pwd:{}'.format(vv['userid'] , vv['password']))


def regexTest():
	# text = 'https://nbamania.com/g2/bbs/board.php?bo_table=multimedia&r=ok'
	# text = 'https://nbamania.com/g2/bbs/board.php?bo_table=multimedia&r=ok'
	# text = 'https://www.pornhub.com/video?c=28/ladifk/idmdi/aiemdj.iklskdsl'
	# rgx = re.compile(r'^http.+(com|edu|net|org)')
	# mo = rgx.search(text)
	# if mo != None:
	# 	# print(dir(mo))
	# 	print(mo.group())


	## case2
	text = 'http://oreilly.com/adfadfafd'	
	text2 = 'https://www.oreilly.com/adfafdadf'
	text3 = 'www.oreilly.com/adfadfaf'
	rgx = re.compile(r'^(http|www).+(com|edu|net|org)')
	mo = rgx.search(text)
	if mo != None:
		s = mo.group().split('.')
		ss=s[-2].split('//')[-1]
		print('s : {}'.format(ss))



def ComprehensionTest():
	global logger
	setLoggingLevel('d')

	#List Comprehension
	events = [x*2 for x in range(0,20)]
	logger.debug('{}'.format(events))

	#Dict Comprehension
	key = ['a' , 'b' , 'c' , 'd' , 'e' , 'f']
	value = [1,2,3,4,5,6]
	dc1 = {k:v for k,v in zip(key,value)}
	logger.debug('dc1 : {}'.format(dc1))

	DC = {k:v+1 for k ,v in  dc1.items()}
	logger.debug('dc : {}'.format(DC))



def FIZZBUZZ():
	for i in range(1,100):
		if i%3 == 0 and i%5 == 0:
			print('{}:FIZZBUZZ'.format(i))
		if i%3 == 0:
			print('{}:FIZZ'.format(i))
		elif i%5 == 0:
			print('{} : BUZZ'.format(i))



def calcProd():
	multi = 1
	for index in range(0,10000):
		if index%1000 == 0:
			print('index : {} ... 1sec sleep...'.format(index))
			time.sleep(2)
		multi = multi * index

	return multi


def bgTimer(quitDate):
	import datetime
	
	while datetime.datetime.now() < quitDate:
		print('{}'.format(datetime.datetime.now()))
		time.sleep(2)


def timeTest():
	import stopWatch
	setLoggingLevel('d')
	s = stopWatch.StopWatch()
	nLab = 1
	lab_dict_ar = []

	## First Start
	s.start()
	try:
		while True:
			input('press enter...')
			# save
			lab_dict = {}
			lab_dict['lab'] = nLab
			lab_dict['lab_time'] = s.stop()
			lab_dict['total_time'] = s.totalTime()
			lab_dict_ar.append(lab_dict)

			# next lab
			nLab +=1
			s.clean().start()

	except KeyboardInterrupt:
		if len(lab_dict_ar) > 0:
			for l in lab_dict_ar:
				# print('{}'.format(list(l)))
				# print('{}'.format(l))
				# print('{}'.format(dir(l)))
				print('='*10)
				for k,v in l.items():
					print('k:{} , v:{}'.format(k,v))
				print('='*10)


def timeTest2():
	import datetime
	import threading

	quitDate = datetime.datetime(2018 , 5 , 27 , 15 , 36 ,0)
	t = threading.Thread(target = bgTimer , args = (quitDate))
	t.start()
	print('end!!!')



## ---------------------------------------------------------------------------------------------------
## 예약 시스템  
## time , datetime , subprocess , thread
## START
def testSubprocess():
	import threading
	t = threading.Thread(target = bgDaemon , args = ('m' , 1 , True))
	t.start()

def bgDaemon(_t , _interval , _infinish):
	import datetime 
	import subprocess

	setLoggingLevel('d')

	start = datetime.datetime.now()
	logger.debug('bg start !!! -- {}'.format(start))
	while True:
		isExecute = False
		cur = datetime.datetime.now()
		if _t == 'h' :
			isExecute = True if isValid(_t , start , cur) == True and (cur.hour - start.hour)%_interval == 0 else False
		elif _t == 'm':
			isExecute = True if isValid(_t , start , cur) == True and (cur.minute - start.minute)%_interval == 0 else False
		else:
			pass

		if isExecute == True:subprocess.Popen('/Applications/GOM Player/GOM Player.app/Contents/MacOS/GOM Player')
		time.sleep(1)


def isValid(_t , _s , _c):
	isValid = False
	if _t == 'h':
		isValid = True if _c.hour - _s.hour > 0 and _c.minute - _s.minute == 0 and _c.second - _s.second == 0 else False
	elif _t == 'm':
		isValid = True if _c.minute - _s.minute > 0 and _c.second - _s.second == 0 else False

	return isValid	

## END
## ---------------------------------------------------------------------------------------------------




def inputPause(_t , _interval):
	import datetime 

	st = datetime.datetime.now()

	while True:
		cu = datetime.datetime.now()
		if st.second  == cu.second - 5:
			print('start sleep :{}'.format(cu))
			time.sleep(_interval)
			print('end sleep : {}'.format(datetime.datetime.now()))

			st = cu




class BBB():
	def __init__(self):
		self.func = {}
		self.func['name'] = self.__setName__
		self.func['age'] = self.__setAge__


	def __setName__(self):
		print('setName')

	def __setAge__(self):
		print('setAge')

	def getaa(self , sss):
		return self.func[sss]()



def print_args(*args):
	print('Position argument tuple:' , args)

def print_kwargs(**args):
	print('Position kwargs dict : ' , args)


def edit(_d):
	return _d.capitalize()+'!'

def edit_plus(_data , func):
	for d in _data:
		print('{}'.format(func(d)))



def echo(anything):
	''' hi
		xferlog
		kknda]
	'''
	return anything


def good(*args):
	return list(args)


class Duck:
	def __init__(self , input_name):
		self.hidden_name = input_name

	@property
	def name(self):
		print('inside the getter')
		return self.hidden_name

	@name.setter
	# @property
	def name(self , input_name):
		print('inside the setter')
		self.hidden_name = input_name



def whois():
	import json
	res = requests.get('http://whois.kisa.or.kr/openapi/whois.jsp?query=202.30.50.51&key=2018071609590114800669&answer=json')
	res.raise_for_status()
	print('{}'.format(res.text))

	jobj = json.loads(res.text)
	for k,v in jobj.items():
		print('{}:{}'.format(k,v))


def testCharacter():
	l = ['a' ,'b','c','d']
	lt = tuple(l.copy())
	print('{}'.format(lt))


def testArray():
	import array
	import binascii

	a = array.array('u' , 'xferlog')
	print('a - len >> {}'.format(len(a)))
	print('a - itemsize >> {}'.format(a.itemsize))

	s = 'this is a array'
	sa = array.array('u' , s)
	print('s >> {}'.format(len(s)))
	print('sa  >> {}'.format(sa))

	# convert binary
	aa = binascii.hexlify(a)
	print('aa type:{} , len : {}'.format(type(aa) , len(aa)))
	print('aa : {}'.format(aa))

	# convert byte
	bb = binascii.unhexlify(aa)
	print('bb type:{} , len : {}'.format(type(bb) , len(bb)))
	print('bb : {}'.format(bb))
	print('str bb : {}'.format(str(bb , encoding='utf-8')))


def str_test():
	print(r'hi\t hello')
	print('hi\t hello')
	spam = 'xferlog kknda kadlf'
	print(spam[:7])

def main():

	init()
	
	
	# testWhois()

	# testCharacter()

	# testArray()

	str_test()

	
if __name__ == '__main__':
	main()
