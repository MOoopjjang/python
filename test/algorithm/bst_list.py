#!python3

'''

reference :
    https://gingerkang.tistory.com/86
    https://zeddios.tistory.com/492
'''

class Node:
    def __init__(self , _l = None , _r = None , _d = None):
        self._left= _l
        self._right= _r
        self._data= _d




class BstMgr:
    def __init__(self):
        self.root = None


    def travelLeft(self):
        if self.root is None:
            return

        current_node = self.root
        while True:
            print(f'data = {current_node._data}')
            if current_node._left is not None:
                current_node = current_node._left
            else:
                break

    def search(self , _v):
        if self.root is None:
            return None

        current_node = self.root
        count = 0;
        while current_node:
            count += 1
            print(f'step .{count} => {current_node._data}')
            if current_node._data == _v:
                return current_node
            elif current_node._data > _v:
                current_node = current_node._left
            elif current_node._data < _v:
                current_node = current_node._right
        return None



    def delete(self , _v):
        '''
        1. target & target panent 찾기
        2. target node와 parent node 연결
          case 1. target node의 자식이 없을경우
          case 2. target node의 자식이 왼쪽만 있을경우
          case 3. target node의 자식이 오른쪽만 있을경우
          case 4. target node의 자식이 양쪽다 있을경우
        '''

        ''' 1.'''
        isSearch = False
        current_node = self.root
        current_node_parent = self.root
        while current_node:
            if current_node._data == _v:
                isSearch = True
                break;
            elif current_node._data > _v:
                current_node_parent = current_node
                current_node = current_node._left
            else:
                current_node_parent = current_node
                current_node = current_node._right

        if isSearch == False:
            return False

        ''' 2. '''
        if current_node._right == None and current_node._left == None:
            if _v < current_node_parent._data:
                current_node_parent._left = None
            else:
                current_node_parent._right = None
        elif current_node._left != None and current_node._right == None:
            current_node = current_node._left
            if _v < current_node_parent._data:
                current_node_parent._left = current_node
            else:
                current_node_parent._right = current_node
        elif current_node._right != None and current_node._left == None:
            current_node = current_node._right
            if _v < current_node_parent._data:
                current_node_parent._left = current_node
            else:
                current_node_parent._right = current_node
        else:
            ''' 
            오른쪽 자식중 가장 작은값을 current_node자리로 대체한다.
            1. 오른쪽 자식중 가장작은 값을 가진 node ( m_node )를 찾는다
            2. 가장 작은 node ( m_node ) 의 부모 ( m_p_node )와 m_node에 자식노드 ( 존재한다면 )를 연결한다.
            3. m_node로 current_node ( 삭제할 노드 )를 대체한다.
               -1. current_node < current_node_parent
                current_node_parent.left = m_node
                m_node.right = current_node.right
                m_node.left = current_node.left
               -2. current_node > current_node_parent
                 current_node_parent.right = m_node
                 m_node.left = current_node.left
                 m_node.right = current_node.right
            '''

            ''' 1.삭제할 node를 대체할 가장 작은 노드 검색 ( 1 , 2 ) 번 수행'''
            c_node = current_node._right
            c_p_node = current_node._right
            while c_node._left != None:
                c_p_node = c_node
                c_node = c_node._left
            if c_node._right != None:
                c_p_node._left = c_node._right
            else:
                c_p_node._left = None

            ''' 2. node를 삭제하고 1.번에서 찾은 node로 대체한다.'''
            if _v < current_node_parent._data:
                current_node_parent._left = c_node
                c_node._left = current_node._left
                c_node._right = current_node._right
            else:
                current_node_parent._right = c_node
                c_node._left = current_node._left
                c_node._right = current_node._right







    def insert(self , _v):
        if self.root is None:
           self.root =  Node(None , None , _v)
           return

        current_node = self.root
        while True:
            if current_node._data > _v:
                if current_node._left != None:
                    current_node = current_node._left
                else:
                    current_node._left = Node(None , None , _v)
                    break
            elif current_node._data < _v:
                if current_node._right is not None:
                    current_node = current_node._right
                else:
                    current_node._right = Node(None , None , _v)
                    break
            else:
                break


if __name__ == '__main__':
    bm = BstMgr()
    ar = [10,4,33,2,23,5,66,3,1,7,9,5]
    for v in ar:
        bm.insert(v)

    while True:
        v = int(input('input num:'))
        print(f'{v}')
        if v == -1:
            break
        print(f'search ###############')
        if bm.search(v) != None:
            print(f'delete ###############')
            bm.delete(v)
            print(f'after ###############')
            if bm.search(v) == None:
                print(f'{v} is not found')

        else:
            print(f'{v} is not found')





