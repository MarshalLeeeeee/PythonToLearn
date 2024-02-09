class T(object):
    
    def __init__(self, data):
        self.data = data

    # def __gt__(self, other):
    #     print '>>> gt'
    #     return self.data > other.data
    def __lt__(self, other):
        print '>>> lt'
        return self.data < other.data
    def __le__(self, other):
        print '>>> le'
        return self.data <= other.data
    def __ne__(self, other):
        print '>>> ne'
        return self.data != other.data
    def __cmp__(self, other):
        print '>>> cmp'
        if self.data > other.data:
            return 1
        elif self.data < other.data:
            return -1
        else:
            return 0

t0 = T(0)
t1 = T(1)
t2 = T(1)
t3 = T(2)
print t0 < t1
print t1 == t2
print t1 != t2
print t3 > t2
'''
>>> lt # use target rich cmp
True
>>> cmp # use base cmp
True
>>> ne # use target rich cmp
False
>>> lt # use the reflection of target rich cmp
True
'''