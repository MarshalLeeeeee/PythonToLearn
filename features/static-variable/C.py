class P(object):
    __slots__ = [
        'v1',
        'v2',
    ]

class PP(P):
    pass

pp = PP()
print 'raw slots:', pp.__slots__
print 'conf: ', dir(pp)
set_v(pp, 'v1', 1)
set_v(pp, 'v2', 2)
set_v(pp, 'v3', 3)
test_weakref(pp)
'''
raw slots: ['v1', 'v2']
conf:  ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__', '__subclasshook__', '__weakref__', 'v1', 'v2']
v1 1
v2 2
v3 3
weakref  <weakref at 0000000003286DB8; to 'PP' at 0000000003286D68> <__main__.PP object at 0x0000000003286D68>
'''