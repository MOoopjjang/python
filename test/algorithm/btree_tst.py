#!python3
# -*- coding:utf-8 -*-

'''
 - 이진트리 테스트
'''

class Node:
    def __init__(self, _data=None):
        self.l = None
        self.r = None
        self.data = _data


def init1(_datas):
    cnode, root = None, None
    lvl = 0
    for data in _datas:
        node = Node(data)
        node.l = None
        node.r = None

        if root is None:
            root = node
            cnode = node
            print('lvl : {} , root : {}'.format(lvl , cnode.data))
        else:
            if cnode.l is None:
                lvl +=1
                cnode.l = node
                print('lvl : {} ,  left : {}'.format(lvl, cnode.l.data))
            else:
                cnode.r = node
                print('lvl : {} , right : {}'.format(lvl, cnode.r.data))
                cnode = node


def init2(datas):
    def addLeftTree(_root , _node):
        cnode = root
        while True:
            if cnode.l is None:
                cnode.l = _node
                break

    def addRightTree(_root , _node):pass

    print('datas : {}'.format(datas))

    root  = None
    for data in datas:
        node = Node(data)
        if root is None:
            root = node
        else:
            addLeftTree(root , node)




if __name__ == '__main__':
    #init(['a','b','c','d','e'])
    init1( [x for x in range(10)])
