#!python3
from module.filter.CorsFilter import CorsFilter
from module.filter.CsrfFilter import CsrfFilter


#from . import CorsFilter as cof
#from . import CsrfFilter as csf

class FilterProxyChain:
    def __init__(self , _filterList):
        self.list = _filterList
        self.count = len(self.list)


    def doFilter(self):
        for filter in self.list:
            filter.doFilter()




if __name__ == '__main__':
    filterProxyChain = FilterProxyChain([CorsFilter() , CsrfFilter()])
    filterProxyChain.doFilter()
