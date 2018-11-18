#!python3 
# -*- coding:utf-8 -*-


import unittest


def simpleFuction(x):
	return x+1


class SimpleFunctionTest( unittest.TestCase ):

	def setUp( self ):
		print('This is run before all of our tests have a change to execute')

	def tearDown( self ):
		print('This is executed after all of out tests have completed')

	def test_simple_function( self ):
		print('Testing that out function works with positive tests')
		self.assertEqual( simpleFuction(2) , 3)
		self.assertEqual( simpleFuction(123456) , 123456)
		self.assertEqual( simpleFuction(0) , 1)


if __name__ == '__main__':
	unittest.main()