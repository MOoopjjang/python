#!python3

'''
 - 파일과 입출력 chepter 테스트코드
'''

def zip_control():
    '''
     - 압축된 데이터 파일 읽고 쓰기
    '''

    import gzip
    import time
    def read(_filename):
        with gzip.open(_filename , 'rt') as f:
            for l in f.readlines():
                print('{}'.format(l))
            # ar = f.readline()

    def write():
        ar = ['xferlog' , 'kknda' ,'bbbbb' , 'ccccc']
        with gzip.open('somefile.gz' , 'wt') as f:
            for t in ar:
                f.write(t+'\n')

            # f.writelines(ar)

    write()
    print(' ----- write complete -----')
    read('somefile.gz')






if __name__ == '__main__':
    zip_control()
