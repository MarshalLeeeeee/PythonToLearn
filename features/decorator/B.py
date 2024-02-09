# pure function decorator implementation
def prefix_deco_func(prefix):
    def deco(func):
        def wrapper(txt):
            txt = prefix + txt
            return func(txt)
        return wrapper
    return deco

@prefix_deco_func('prefix_deco_func: ')
def test_func_deco(txt):
    print(txt)

test_func_deco('test_func_deco') # prefix_deco_func: test_func_deco

# class decorator + function decorator serve as class decorator factory
class PrefixDecoCls(object):

    def __init__(self, func, prefix):
        self._func = func
        self._prefix = prefix

    def __call__(self, txt, *ignores):
        self._func(self._prefix + txt)

def prefix_deco_cls(prefix):
    def deco_cls_factory(func):
        return PrefixDecoCls(func, prefix)
    return deco_cls_factory

@prefix_deco_cls('prefix_deco_cls: ')
def test_func_cls(txt):
    print(txt)

test_func_cls('test_func_cls') # prefix_deco_cls: test_func_cls