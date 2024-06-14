#!python3

#######################################################
#
#    Java의 Bean factory같은 기능을 python으로 구현..
#
#######################################################

class ApplicationContex:
    def __init__(self):
        self.factory = {}
        self._load_()

    def _load_(self):
        import json
        import importlib
        with open('config.json', 'rt', encoding="utf-8") as fr:
            jsonObj = json.load(fr)
            for info in jsonObj['list']:
                c = info['class']

                ss = c.split('.')
                className = ''.join(ss[-1:])
                module = '.'.join(ss[:-1])
                print(f'className = {className} , module = {module}')

                m = importlib.import_module(module)
                bean = getattr(m, className)
                self.factory[className] = bean()

    def getBean(self, _beanName):
        return self.factory[_beanName]


if __name__ == '__main__':
    appContext = ApplicationContex()
    person = appContext.getBean("Person")
    print(f'person = {person}')
