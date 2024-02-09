import functools

@functools.total_ordering
class P(object):
    
    def __init__(self, data):
        self.data = data           
    def __le__(self, other):
        print '>>> le'
        return self.data <= other.data
    def __eq__(self, other):
        print '>>> eq'
        return self.data == other.data
        
p0 = P(0)
p1 = P(1)
p2 = P(1)
p3 = P(2)
print p0 < p1
print p1 == p2
print p1 != p2
print p3 > p2
'''
>>> le
>>> eq
True
>>> eq
True
>>> eq
False
>>> le
True
'''