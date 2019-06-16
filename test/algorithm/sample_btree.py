#!python3
#-*- coding:utf-8 -*-

root = None

class Node:
    def __init__( self , data ):
        self.data = data
        self.left = None
        self.right = None


# 전위 순회 알고즘즘즘
def preorder_traverse( node ):
    if node == None:return

    print(node.data , end='-->')
    preorder_traverse(node.left)
    preorder_traverse(node.right)



# 중위 순회 알고리즘
def inorder_traverse( node ):
    if node == None:return

    inorder_traverse(node.left)
    print(node.data , end='-->')
    inorder_traverse(node.right)


# 후위순회 알고리즘
def postorder_traverse( node ):
    if node == None:return

    postorder_traverse( node.left )
    postorder_traverse( node.right )
    print(node.data , end = '-->')



def init_tree():
    global root

    root = Node('A')
    nNode = Node('B')
    root.left = nNode
    nNode = Node('C')
    root.right = nNode

    node = root.left
    nNode = Node('D')
    node.left = nNode
    nNode = Node('E')
    node.right = nNode

    node = root.right
    nNode = Node('F')
    node.left = nNode
    nNode = Node('G')
    node.right = nNode



levelq = []



def levelorder_traverse( node ):
    global levelq

    levelq.append( node )
    while len(levelq)!=0:
        # visit
        visit_node = levelq.pop(0)
        print(visit_node.data , end='->')
        #child put
        if visit_node.left != None:
            levelq.append( visit_node.left )

        if visit_node.right != None:
            levelq.append( visit_node.right )




if __name__ == '__main__':
    init_tree()

    print('<Preorder Traverse >')
    preorder_traverse(root)
    print('\n')
    print('<Inorder Traverse >')
    inorder_traverse(root)
    print('\n')
    print('<Postorder Traverse >')
    postorder_traverse(root)
    print('\n')
















































