#!python3
#-*- coding:utf8 -*-


def mlist_test():
	from mlist_container import mlist

	m = mlist()
	m.push('xferlog').push('kknda').push('hi').push('kcwda')

	print('>>{}'.format(m.__next__()))
	print('>>{}'.format(m.__next__()))
	print('>>{}'.format(m.__next__()))




def countdown(n):
	print('>> {}'.format(n))
	while n > 0:
		yield n
		n -= 1
	# return


def main():
	# c = countdown(10)
	# for i in range(0,5):
	# 	print(c.__next__())

    mlist_test()





if __name__ == '__main__':
	main()