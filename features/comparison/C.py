class T(object):
    
    def __init__(self, data):
        self._data = data

    def __repr__(self):
        return '__T__repr__' + str(self._data)
        
    def __eq__(self, other):
        return abs(self._data) == abs(other._data)
        
    def __gt__(self, other):
        return True
        
    def __lt__(self, other):
        return True
        
    def __ge__(self, other):
        return True
        
    def __le__(self, other):
        return True

t1 = T(1)
t2 = T(-1)
print(t1==t2)
print(t1!=t2)
l = [t1, t2, t1]
l.sort()
print(l)
l.sort(reverse=True)
print(l)
'''
True
True
[__T__repr__1, __T__repr__-1, __T__repr__1]
[__T__repr__1, __T__repr__-1, __T__repr__1]
'''