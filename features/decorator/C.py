class ClsDecoFuncWrapper(object):

    def __init__(self, func, prefix, suffix):
        self._func = func
        self._prefix = prefix
        self._suffix = suffix

    def __call__(self, *args, **kwargs):
        print('==================================')
        print('>>>> Cls Deco Head: ', self._prefix)
        _res = self._func(*args, **kwargs)
        print('>>>> Cls Deco Tail: ', self._suffix)
        return _res

class ClsDecoParamWrapper(object):

    def __init__(self, prefix, suffix):
        self._prefix = prefix
        self._suffix = suffix

    def __call__(self, func):
        return ClsDecoFuncWrapper(func, self._prefix, self._suffix)

@ClsDecoParamWrapper('p1', 's1')
def test_print(txt):
    print('print something: ', txt)

@ClsDecoParamWrapper('p2', 's2')
def test_calc(x, y):
    return x+y

test_print('blabla')
_sum = test_calc(3, 4)
print(_sum)
'''
==================================
>>>> Cls Deco Head:  p1
print something:  blabla
>>>> Cls Deco Tail:  s1
==================================
>>>> Cls Deco Head:  p2
>>>> Cls Deco Tail:  s2
7
'''





class ClsDeco(object):

    def __init__(self, prefix, suffix, func=None):
        self._prefix = prefix
        self._suffix = suffix
        self._func = func

    def __call__(self, *args, **kwargs):
        if self._func is None:
            self._func = args[0]
            return self
        else:
            print('==================================')
            print('>>>> Cls Deco Head: ', self._prefix)
            _res = self._func(*args, **kwargs)
            print('>>>> Cls Deco Tail: ', self._suffix)
            return _res

@ClsDeco('np1', 'ns1')
def test_print(txt):
    print('print something: ', txt)

@ClsDeco('np2', 'ns2')
def test_calc(x, y):
    return x+y

test_print('blabla')
_sum = test_calc(3, 4)
print(_sum)
'''
==================================
>>>> Cls Deco Head:  np1
print something:  blabla
>>>> Cls Deco Tail:  ns1
==================================
>>>> Cls Deco Head:  np2
>>>> Cls Deco Tail:  ns2
7
'''