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
	sales3.xls
	apac1.xls
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

	print('{}'.format(text4))


	rgx = re.compile('[ns]a[^0-9]\.xls')  # text1
	# rgx = re.compile('#[0-9A-Z]{6}') #text4
	mo = rgx.findall(text1)
	if mo != None:print('{}'.format(mo))


def main():
	# test1()
	test2()

if __name__ == '__main__':
	main()



