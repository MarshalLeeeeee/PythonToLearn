import weakref

class T(object):
    pass

class TS(object):
    __slots__ = (
        'v1',
        'v2',
    )

class TSWR(object):
    __slots__ = (
        'v1',
        'v2',
        '__weakref__',
    )

class TSWRD(object):
    __slots__ = (
        'v1',
        'v2',
        '__weakref__',
        '__dict__',
    )

def set_v(t, vs, v):
    try:
        setattr(t, vs, v)
        print vs + ' ' + str(getattr(t, vs))
    except:
        print vs + ' [Not exist] '

def test_weakref(t):
    try:
        _twr = weakref.ref(t)
        print 'weakref ', _twr, _twr()
    except:
        print 'weakref [Not exist] '

t = T()
print ' === tv === '
print 'tconf:', dir(t)
set_v(t, 'v1', 1)
set_v(t, 'v2', 2)
set_v(t, 'v3', 3)
test_weakref(t)
'''
 === tv === 
tconf: ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
v1 1
v2 2
v3 3
weakref  <weakref at 00000000037D6B38; to 'T' at 00000000037D95C8> <__main__.T object at 0x00000000037D95C8>
'''

ts = TS()
print ' === tsv === '
print 'tsconf:', dir(ts)
set_v(ts, 'v1', 1)
set_v(ts, 'v2', 2)
set_v(ts, 'v3', 3)
test_weakref(ts)
'''
 === tsv === 
tsconf: ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', 'v1', 'v2']
v1 1
v2 2
v3 [Not exist] 
weakref [Not exist] 
'''

tswr = TSWR()
print ' === tswrv === '
print 'tswrconf:', dir(tswr)
set_v(tswr, 'v1', 1)
set_v(tswr, 'v2', 2)
set_v(tswr, 'v3', 3)
test_weakref(tswr)
'''
 === tswrv === 
tswrconf: ['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', 'v1', 'v2']
v1 1
v2 2
v3 [Not exist] 
weakref  <weakref at 00000000037D6B38; to 'TSWR' at 00000000037D96C8> <__main__.TSWR object at 0x00000000037D96C8>
'''

tswrd = TSWRD()
print ' === tswrdv === '
print 'tswrdconf:', dir(tswrd)
set_v(tswrd, 'v1', 1)
set_v(tswrd, 'v2', 2)
set_v(tswrd, 'v3', 3)
test_weakref(tswrd)
'''
 === tswrdv === 
tswrdconf: ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', 'v1', 'v2']
v1 1
v2 2
v3 3
weakref  <weakref at 00000000037D6B88; to 'TSWRD' at 00000000037D6B38> <__main__.TSWRD object at 0x00000000037D6B38>
'''