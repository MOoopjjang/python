#!python
#-*- coding:utf-8 -*-


import logging

def init():
	global logger
	logging.basicConfig(level = logging.DEBUG , format = '%(asctime)s - %(levelname)s - %(message)s')
	logger = logging.getLogger(__file__)

def setLoggingLevel(_lvl):
	global logger
	logger.setLevel(logging.DEBUG) if _lvl == 'd' else logger.setLevel(logging.INFO)


def LC():
	global logger
	setLoggingLevel('d')
	logger.debug('-'*10+'lc start'+'-'*10)
	lc1 = [v*2 for v in range(0,10)]
	logger.debug('lc1 : {}'.format(lc1))



def DC():
	global logger
	logger.debug('-'*10+'dc start'+'-'*10)
	keys = ['xferlog' , 'kknda' , 'kthda' , 'ejkim']
	values = [1,2,3,4]

	dc1 = {k:v for k,v in zip(keys,values)}
	logger.debug('dc1 : {}'.format(dc1))

	dc2 = {k:v+10 for k,v in dc1.items()}
	logger.debug('dc2 : {}'.format(dc2))


def main():
	init()
	LC()
	DC()


if __name__ == '__main__':
	main()