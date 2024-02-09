class T(object):
    
    def __init__(self, data):
        self._data = data

    def __repr__(self):
        return '__T__repr__' + str(self._data)
        
    def __eq__(self, other):
        return abs(self._data) == abs(other._data)
        
    def __hash__(self):
        return hash(self._data)
        
d = {}
t1 = T(1)
t2 = T(-1)
print(t1 == t2)
d.update({t1:t1})
print(d)
d.update({t2:t2})
print(d)
t1._data = -1
print(d)
'''
True
{__T__repr__1: __T__repr__1}
{__T__repr__1: __T__repr__1, __T__repr__-1: __T__repr__-1} # publicly equal objects do not share the same key
{__T__repr__-1: __T__repr__-1, __T__repr__-1: __T__repr__-1} # after key changed, the dict is not updated
'''