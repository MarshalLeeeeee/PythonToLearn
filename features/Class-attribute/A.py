class P(object):

    __slots__ = (
        'x',
        'y',
    )

    def __getattr__(self, name):
        print "getattr", name
        return None

    def __setattr__(self, name, value):
        print "setattr", name, value
        if name in self.__slots__:
            super(P, self).__setattr__(name, value)
        else:
            print '>>> name %s not in __slots__ for set' % name

    def __delattr__(self, name):
        if getattr(self, name) is not None:
            super(P, self).__delattr__(name)
        else:
            print '>>> name %s not in __slots__ for del' % name

p = P()
print p.x
print p.y
print p.z
print p.__slots__
'''
getattr x
None
getattr y
None
getattr z
None
('x', 'y')
'''

p.x = 1
p.y = 1
p.z = 1
print p.x
print p.y
print p.z
print p.__slots__
'''
setattr x 1
setattr y 1
setattr z 1
>>> name z not in __slots__ for set
1
1
getattr z
None
('x', 'y')
'''

del p.x
del p.z
print p.x
print p.y
print p.z
print p.__slots__
'''
delattr x
delattr z
getattr z
>>> name z not in __slots__ for del
getattr x
None
1
getattr z
None
('x', 'y')
'''