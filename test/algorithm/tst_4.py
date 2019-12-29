#!python3
#-*- coding:utf -*-


def tst1():
    '''
    파일의 단어 반복 횟수 출력
    '''
    import collections
    class WordCounter:
        def __init__( self , _wordfile = None ):
            if _wordfile is None:
                raise FileExistsError('parameter error')

            self._wordfile = _wordfile
            self._d = collections.defaultdict(int)

        def run( self ):
            with open(self._wordfile , 'r') as fr:
                for line in fr:
                    s = line.split()
                    for ss in s:
                        self._d[ss]+=1
            return self


        def result( self ):
            for k,v in self._d.items():
                print('{}:{}'.format(k,v))


    wc = WordCounter('sample_2.txt')
    wc.run().result()



if __name__ == "__main__":
    tst1()