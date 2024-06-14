#!python3


class CorsFilter:
    def __init__(self):
        self.name = "cors"

    def doFilter(self):
        print(f'{self.name} filter!!')
