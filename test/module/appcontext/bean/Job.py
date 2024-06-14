#!python3



class Job:
    def __init__(self):
        self.companyName = 'wizard'
        self.kind = 'programmer'

    def __str__(self):
        return f'companyName={self.companyName} , kind={self.kind}'


if __name__ == '__main__':
    j = Job()
    print(f'j = {j}')