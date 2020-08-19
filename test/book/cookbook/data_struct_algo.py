#!python3
# -*- coding:utf -*-



def heapq_tst():
    '''
    1.5 우선 순위 큐 구현

    주어진 우선 순위에 따라 아이템을 정렬하는 큐를 구헌햐고 항상 우선 순위가 가장 높은 아이템을 먼저 팝하도록 만들어야 한다.
    '''
    import heapq
    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def __iter__(self):
            return (item for item in self._queue)

        def push(self , item , priority):
            heapq.heappush(self._queue , (-priority , self._index , item))
            self._index += 1
        def pop(self):
            return heapq.heappop(self._queue)[-1]

    class Item:
        def __init__(self , name):
            self._name = name
        def __repr__(self):
            return 'Item({!r})'.format(self._name)

   # TEST Coding
    pq = PriorityQueue()
    pq.push(Item('cwkim') , 1)
    pq.push(Item('aaaa') , 5)
    pq.push(Item('khlee') , 3)

    print('-'*20)
    for item in pq:
        print(item)
    print('-'*20)
    print(pq.pop())
    print(pq.pop())
    print(pq.pop())





def tst1():
    '''순환체를 언패킹하려는데 요소가 N개 이상 포함되어 "값이 너무 많습니다."라는 예외가 발생한다.'''

    ar = ['a' , 'b' , 'c' , 'd' , 'e']
    a,*middle,e = ar
    print('a : {} , e : {}'.format(a , e))
    print('middle : {}'.format(middle))

    print('-'*30)
    record = ('Dave' , 'aaa@bbb.com' , '1112223333','44455556666')
    name , email , *ph = record
    print('name : {} , email : {}'.format(name , email))
    print('phone: {}'.format(ph))


if __name__ =='__main__':
    # tst1()
    heapq_tst()

