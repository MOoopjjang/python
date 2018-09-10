#!python
#-*- encoding:utf-8 -*-


import re



def test1():
	text1 = """hi there can i speak xferlog@aaa.com english?my speaking phone speak is 010-9811-3963 speak address
	"""

	text2 = 'http://www.naver.com'
	text3 = '/image/aalfkalf'

	# pattern1 = '[0-9]{3}-[0-9]{3,}-[0-9]{4}'
	# pattern1 = '[0-9]{3}(-[0-9]{4}){2}'
	pattern1 = '\d{3}(-\d{4}){2}'
	pattern2 = 'speak'
	pattern3 = 'http?'
	pattern4 = 'speak[a-zA-Z]*'

	print('text1 >> {}'.format(text1))
	# rgx = re.compile(pattern2)
	rgx = re.compile(pattern4)
	mo = rgx.findall(text1)
	if mo != None:
		print('{}'.format(dir(mo)))
		# rint('{}'.format(mo))
		print('len>>{}'.format(len(mo)))
		print('mo>>{}'.format(mo))



def test2():
	text = """
	hello, my name is Ben , Please visit
	my website at http://www.forta.com/.
	"""

	text1 = """
	sales.xls
	sales1.xls
	order3.xls
	sales2.xls
	ca7.xls
	sales3.xls
	apac1.xls
	ca10.xls
	europe2.xls
	sam.xls
	ca1.xls
	na1.xls
	na2.xls
	sa1.xls
	"""

	text3 = """
	The phrase 'regular expression' is often
	abbreviated as RegEx or regex.
	"""

	text4 = """
	<BODY BGCOLOR='#336633' TEXT='#FFFFFF'
		  MARGINWIDTH='0' MARGINHEIGHT='0' TOPMARGIN='0'
		  LEFTMARGIN='0'
	"""


	text5 = """
	var array = new Array()
	...
	if(array[0] === 'xferlog'){
	   console.log('kkllkll')
	}
	"""


	text6 = """
	'101','Ben','Forta'
	'102','Jim','James'

	'103','Roberta','Robertson'
	'104','Bob','Bobson'
	"""

	text7 = """
	11213
	A1C2E3
	48075
	78237
	M1B4F2
	90046
	H1H2H2
	"""


	text8 = """
	Send personal email to ben@forta.com. For questions
	about a book use support@forta.com. Feel free to send
	unsolicited email to spam@forta.com (wouldn't it be
	nice if it were that simple, huh?).
	"""

	text9 = """
	Send personal  bbb.ccc.ccc@ttt.com email to ben@forta.com or
	ben.forta@forta.com. For questions about a
	book use support@forta.com. If your message
	is urgent try ben@urgent.forta.com. Feel
	free to send unsolicited email to
	spam@forta.com (wouldn't it be nice if
	it were that simple, huh?).
	"""

	text10 = """
	Hello .ben@forta.com is my email address.
	"""

	text11= """
	The URL is http://www.forta.com/ , to connect
	securely use https://www.forta.com/ instead.
	"""

	text12 = """
	4/8/03
	10-6-2004
	2/2/2
	01-01-01
	"""

	print('{}'.format(text12))


	# rgx = re.compile('[ns]a[^0-9]\.xls')  # text1
	# rgx = re.compile('#[0-9A-Z]{6}') #text4
	# rgx = re.compile('[cn]a[\d]{1,}\.xls')
	# rgx = re.compile('\r\n\r\n') #text6
	# rgx = re.compile('\w\d\w\d\w\d') #text7
	# rgx = re.compile('\w+[\w.]*@[\w\.]+\.\w+') #text8
	# rgx = re.compile('https?://[\w.]+\.\w+/') #text11
	# rgx = re.compile('#[\w\d]{6}') #text11
	rgx = re.compile('\d{1,2}[-\/]\d{1,2}[-\/]\d{2,4}') #text12
	mo = rgx.findall(text12)
	if mo != None:print('{}'.format(mo))


def main():
	# test1()
	test2()

if __name__ == '__main__':
	main()



