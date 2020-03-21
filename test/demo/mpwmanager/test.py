#!python3
#-*- coding:utf-8 -*-


from mauthenticationmanager import MAuthenticationManager



def tst_auth():
	m = MAuthenticationManager()
	m.createMember('aaaa@aaaa.com' , '1111')

	input_email = input('email:')
	input_pw = input('pw:')

	ret = m.certification(input_email , input_pw)
	print('{}'.format(ret))




def main():pass
	



if __name__ == '__main__':
	tst_auth()