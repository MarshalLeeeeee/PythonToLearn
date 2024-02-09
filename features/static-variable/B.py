class P(object):
    __slots__ = [
        'v1',
        'v2',
    ]

p = P()
print 'raw slots:', p.__slots__
p.__slots__.extend(['v3', '__weakref__', '__dict__'])
print 'mutated slots:', p.__slots__
set_v(p, 'v1', 1)
set_v(p, 'v2', 2)
set_v(p, 'v3', 3)
test_weakref(p)
'''
raw slots: ['v1', 'v2']
mutated slots: ['v1', 'v2', 'v3', '__weakref__', '__dict__']
v1 1
v2 2
v3 [Not exist] 
weakref [Not exist] 
'''