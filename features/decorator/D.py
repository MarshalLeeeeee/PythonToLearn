class DecoClass(object):

    _funcs = []

    def __init__(self, func):
        DecoClass._funcs.append(func)

    def __call__(self):
        print(len(self._funcs))
        for _func in self._funcs:
            _func()

@DecoClass
def foo():
    print('foo')

@DecoClass
def bar():
    print('bar')

@DecoClass
def cat():
    print('cat')

foo()
'''
3
foo
bar
cat
'''

#######

g = 0

def deco(func):
    def wrapper():
        global g
        g += 1
        print('Deco Head', g)
        func()
        print('Deco Tail', g)
    return wrapper

@deco
def foo2():
    print('foo2')

@deco
def bar2():
    print('bar2')

@deco
def cat2():
    print('cat2')

foo2()
'''
Deco Head 1
foo2
Deco Tail 1
'''