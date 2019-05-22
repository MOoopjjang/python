#!python3
#-*- coding:utf-8 -*-


from configmanager import ConfigMgr
from mifchecker import IfChecker

import os , sys


def main():
	conf = ConfigMgr(sys.argv[1])
	checker = IfChecker(conf)
	checker.run()



if __name__ == '__main__':
	main()