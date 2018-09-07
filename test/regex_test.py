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



def main():
	test1()

if __name__ == '__main__':
	main()



