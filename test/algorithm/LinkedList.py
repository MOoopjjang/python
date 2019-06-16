#!python3
#-*- coding:utf-8 -*-



"""
 Linked List Test Code
"""


class Node:
	def __init__( self , _data , _next = None , _prev = None ):
		self.prev = _prev
		self.next = _next
		self.data = _data




class SingleLinkedList:
	def __init__( self ):
		"""
		Single LinkedList
		"""
		self._firstNode = None
		self._lastNode = None



	def __iter__( self ):
		cNode = self._firstNode
		while cNode != None:
			v = cNode.data
			cNode = cNode.next
			yield v


	def put(self , _node):
		if self._firstNode == None:
			self._firstNode = _node
			self._firstNode.next = self._firstNode
		else:
			self._lastNode.next = _node

		self._lastNode = _node


	def get( self , _v):
		cNode = self._firstNode
		while True:
			if cNode.data == _v:
				return cNode
			
			cNode = cNode.next
			if cNode.next == None:break


	def remove(self , _del_v ):
		cNode = self._firstNode
		pNode = None
		nNode = cNode.next
		while True:
			if cNode.data == _del_v:
				if cNode == self._firstNode:
					self._firstNode = cNode.next
				else:
					pNode.next = nNode
				break

			pNode = cNode
			cNode = cNode.next
			nNode = cNode.next





class DoubleLinkedList:
	def __init__( self ):
		self.firstNode = None
		self.lastNode = self.firstNode


	def __iter__( self ):
		cNode = self.firstNode
		while cNode != None:
			result = cNode.data
			cNode = cNode.next
			yield result


	def put( self , _node ):
		if self.firstNode == None:
			self.firstNode = _node
		else:
			_node.prev = self.lastNode
			self.lastNode.next = _node
			self.lastNode = _node

		self.lastNode = _node


	def insert( self , t_data ,n_node  , _m = 'after'):
		cNode = self.firstNode
		pNode = None
		nNode = None
		while cNode != None:
			if cNode.data == t_data:
				pNode = cNode.prev
				nNode = cNode.next
				break

			cNode = cNode.next

		if _m == 'before':
			n_node.next = cNode
			n_node.prev = pNode
			pNode.next = n_node
		else:
			n_node.next = nNode
			n_node.prev = cNode
			cNode.next = n_node


	def get( self , _v ):
		cNode = self.firstNode
		result = None
		while cNode != None:
			if cNode.data == _v:
				result = cNode.data
				break

			cNode = cNode.next
		return result


	def find( self , _v ):
		cNode = self.firstNode
		c = None
		p = None
		n = None
		while cNode != None:
			if cNode.data == _v:
				c = cNode.data
				p = cNode.prev.data
				n = cNode.next.data
			cNode = cNode.next

		return (c,p,n)


	def remove( self , _v ):
		cNode = self.firstNode
		pNode = cNode.prev
		nNode = cNode.next
		while True:
			if cNode.data == _v:
				if self.firstNode == cNode:
					self.firstNode = cNode.next
					self.firstNode.prev = None
				elif self.lastNode == cNode:
					self.lastNode = cNode.prev
					self.lastNode.next = None
				else:
					pNode = cNode.prev
					nNode = cNode.next

					pNode.next = nNode
					nNode.prev = pNode
				break


			pNode = cNode
			cNode = cNode.next
			nNode = cNode.next




def single_linkedlist_test():
	sm = SingleLinkedList()
	sm.put(Node('xferlog'))
	sm.put(Node('kknda'))
	sm.put(Node('ejkim'))
	sm.put(Node('bhkim'))
	sm.put(Node('hyun'))

	print('-'*20)
	for v in sm:
		print(v)

	print('-'*20)
	print('remove : xferlog')
	sm.remove('xferlog')
	print('-'*20)

	for v in sm:
		print(v)
	print('-'*20)


def double_linkedlist_test():
	dm = DoubleLinkedList()
	dm.put(Node('xferlog'))
	dm.put(Node('kknda'))
	dm.put(Node('ejkim'))
	dm.put(Node('bhkim'))
	dm.put(Node('hyun'))

	print('-'*20)
	for v in dm:
		print(v)
	print('-'*20)

	c,p,n = dm.find('ejkim')
	print('c : %s , p : %s , n : %s'%(c,p,n))
	print('-'*20)

	print('remove : xferlog')
	dm.remove('xferlog')
	print('-'*20)

	for v in dm:
		print(v)
	print('-'*20)


	dm.insert('ejkim' , Node('aaaa') , 'before')
	print('-'*20)

	for v in dm:
		print(v)
	print('-'*20)






if __name__ == '__main__':
	# single_linkedlist_test()

	double_linkedlist_test()

	










