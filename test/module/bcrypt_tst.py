#!python3
#-*- coding:utf-8 -*-

'''
	암호화 모듈 테스트 ( bcrypt )
'''

import bcrypt

def default():
	passwd = b'1111'

	salt = bcrypt.gensalt()
	hashed = bcrypt.hashpw(passwd , salt)

	print('salt : {}'.format(salt))
	print('hashed : {}'.format(hashed))


	inputpwd = input('passwd :')
	if bcrypt.checkpw(inputpwd.encode() , hashed):
		print('matched')
	else:
		print('not matched')




if __name__ == '__main__':
	default()