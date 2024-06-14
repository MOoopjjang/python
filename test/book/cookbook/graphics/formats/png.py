

def t1():
    return "t1"

def t2():
    return "t2"


privateName='xferlog'


# 't1'과 't2'만 내보낸다
__all__ = ['t1' , 't2']