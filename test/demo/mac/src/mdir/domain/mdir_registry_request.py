#!python3


from src.common.domain.base_domain import BaseDomain

class MDirRegistryRequest( BaseDomain ):
    def __init__(self , _name , _path):
        self.name = _name
        self.path = _path