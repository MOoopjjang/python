#!python3
#-*- coding:utf-8 -*-



"""
 2 진트리를 만들기위한 조건
  - 레벨 검색 필요

"""


class Node:
	def __init__( self , data ):
		self.data = data
		self.left = None
		self.right = None


class MBTree:
	def __init__( self ):
		self.root = None
		self.depth = 0



	def insert( self , _data ):
		nNode = Node(_data)

		sNode = self.root
		while True:
			rNode = self.__insertPosition(sNode)
			if rNode == None:break


		rNode = nNode


	def __insertPosition( self , _node ):
		if _node == None:return _node

		if _node.left == None:return _node.left
		if _node.right == None:return _node.right

		# self.__insertPosition(_node.left)











