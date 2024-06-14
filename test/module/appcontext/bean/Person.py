#!python3


class Person:
    def __init__(self):
        self.name = 'xferlog'
        self.age = 20

    def __str__(self):
        return f'name={self.name} , age = {self.age}'


if __name__ == '__main__':
    p = Person()
    print(f'p = {p}')
