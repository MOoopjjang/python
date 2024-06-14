#!python3


class CsrfFilter:
    def __init__(self):
        self.name = 'csrf'

    def doFilter(self):
        print(f'{self.name} filter!!!')
