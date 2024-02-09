class P(object):

    __slots__ = (
        'x',
        'y',
    )

    def __getattr__(self, name):
        print(">>> getattr", name)
        return None

    def __getattribute__(self, name):
        print(">>> getattribute", name)
        return super(P, self).__getattribute__(name)

    def __setattr__(self, name, value):
        print(">>> setattr", name, value)
        if name in self.__slots__:
            super(P, self).__setattr__(name, value)
        else:
            print('>>> name %s not in __slots__ for set' % name)

    def __delattr__(self, name):
        print(">>> delattr", name)
        if getattr(self, name) is not None:
            super(P, self).__delattr__(name)
        else:
            print('>>> name %s not in __slots__ for del' % name)

p = P()
p.x = 1
p.y = 1
p.z = 1
print(p.x)
print(p.y)
print(p.z)
print(p.__slots__)
'''
>>> setattr x 1
>>> getattribute __slots__
>>> setattr y 1
>>> getattribute __slots__
>>> setattr z 1
>>> getattribute __slots__
>>> name z not in __slots__ for set
>>> getattribute x
1
>>> getattribute y
1
>>> getattribute z
>>> getattr z
None
>>> getattribute __slots__
('x', 'y')
'''