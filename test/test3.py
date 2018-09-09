#!python3
#-*- coding:utf-8 -*-



import os , sys
from unicodedata import normalize



def t1():
	cdir = os.getcwd()+'/tt'

	for d , s , fs in os.walk(cdir):
		for f in fs:
			dd = os.path.join(d , f)
			# print('{} : {}'.format(dd , len(dd)))
			filename = normalize('NFC', dd)
			# print('{} : {}'.format(dd , len(dd)))
			print('{} : {}'.format(filename , len(filename)))

	inp = input('>>')
	print('{} : {}'.format(inp , len(inp)))


def t2():
	strkey = 'aaa|bbb'
	# strkey = 'name'
	s = set(strkey.split('|'))
	print('{}'.format(s))

	d = {}
	person = {}
	person['name'] = 'xferlog'
	person['age'] = 20

	company = {}
	company['name'] = 'zinna'
	company['addr'] = 'incheon'


	d['person'] = person
	d['comp'] = company

	# for key in d['person'].keys():
	# 	if key in s:
	# 		print('{} : {}'.format(key , d['person'][key]))
	

	s1 = set(d['person'].keys())
	# print('s1 -- {}'.format(s1))	

	s2 = s & s1	
	s3 = s - s1

	print('> common => {}'.format(s2))
	print('> diff ==> {}'.format((s3)))

	# for key in s2:
	# 	print('s2----{}'.format(key))


def t3():
	olist = [i for i in range(1 , 10) if i%2 == 0]
	print('olist : {}'.format(olist))

	# *result* = [*transform* , *iteration* , *filter*]
	# print('*result* ==> {}'.format(result))


	olist2 = [i**2 for i in range(0,10)]
	print('olist2 : {}'.format(olist2))


	# string = 'hello 123kdk45 kknda'

	# aaa = ','.join(string_digit) = [x for x in string if x.isdigit()]
	# print('{}'.format(aaa))


def t4():
	sample = '✷✔︎▲☛✘❒❡'
	hi = [ord(x) for x in sample if ord(x) > 127]
	print('{}'.format(hi))

	hii = list(filter(lambda c:c > 127 , map(ord , sample)))
	print('{}'.format(hii))


def smtp_test():
	import smtplib
	from email.mime.text import MIMEText

	msg = MIMEText('The body of the email is here')

	msg['Subject'] = 'An Email Alert'
	msg['From'] = 'aaaa@naver.com'
	msg['To'] = 'bbbb@gmail.com'

	s = smtplib.SMTP( 'localhost' )
	s.send_message( msg )
	s.quit()



def main():
	# t1()
	# t2()

	# t3()

	# t4()
	smtp_test()



if __name__ == '__main__':
	main()

