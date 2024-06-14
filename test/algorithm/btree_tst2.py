#!/bin/python


'''
- 이진트리 저장/검색/삭제/순회
'''


class BNode:
    def __init__(self, v=None, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

    def __str__(self):
        return f'value = {self.value} , left = {self.left} , right = {self.right}'


class BTree:
    def __init__(self):
        self.root = None

    '''
    삽입
    '''

    def insert(self, node):
        if not self.root:
            self.root = node
            return

        def bfs(curNode):
            if not curNode:
                return node

            if curNode.value < node.value:
                curNode.right = bfs(curNode.right)
            else:
                curNode.left = bfs(curNode.left)

            return curNode

        bfs(self.root)

    def find(self, key):
        cur = self.root

        while cur:
            if cur.value == key:
                break

            if cur.value < key:
                cur = cur.right
            else:
                cur = cur.left

        return cur if cur.value == key else None

        '''
                    [7]                     [7]
                   /   \                   /   \
        del->    [4]   [9]               [3]
                /   \                   /   \
              [3]  [5]                [1]  [2]
            /    \                           \
          [1]   [2]                         [5]
        '''
    def remove_node(self , key):
        pass


    def pre_order(self , cur):
        print(cur.value , end=' ')
        if cur.left:
            self.pre_order(cur.left)

        if cur.right:
            self.pre_order(cur.right)





if __name__ == '__main__':
    btree = BTree()
    btree.insert(BNode(v=10))
    btree.insert(BNode(v=9))
    btree.insert(BNode(v=11))
    btree.insert(BNode(v=20))
    btree.insert(BNode(v=5))
    btree.insert(BNode(v=7))

    r = btree.find(11)
    print(r)
    print('*'*20)
    btree.pre_order(btree.root)
