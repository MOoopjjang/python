#!python3
#-*- coding:utf-8 -*-


from mauthenticationmanager import MAuthenticationManager



def auth_init( _manager ):
	_manager.createMember('khlee@zinnaworks.com' , 'khlee123')
	_manager.createMember('cwkim@zinnaworks.com' , 'cwkim123')
	
def tst_auth():
	m = MAuthenticationManager()
	auth_init(m)

	# m.removeMember('cwkim@zinnaworks.com')

	while True:
		input_email = input('email:')
		input_pw = input('pw:')

		if input_email=='q':break

		ret = m.certification(input_email , input_pw)
		print('{}'.format(ret))



def main():
	SAMPLE_DICT = {'name':'xferlog' , 'age':20}

	print('{}'.format(SAMPLE_DICT))	

	del SAMPLE_DICT['name']
	print('{}'.format(SAMPLE_DICT))	



if __name__ == '__main__':
	tst_auth()
	# main()