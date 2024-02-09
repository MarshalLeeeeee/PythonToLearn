import traceback

class T(object):
    
    def __init__(self, data):
        self._data = data
    
    def __iadd__(self, other):
        print '>>> %s self add' % self
        self._data += other._data
        return self
        
    def __str__(self):
        return ' < %s %d > ' % (type(self).__name__, self._data)
        
class P(T):

    def __radd__(self, other):
        print '>>> %s right add %s' % (self, other)
        return type(self)(other._data + self._data)
        
class Q(T):
    
    def __add__(self, other):
        print '>>> %s left add %s' % (self, other)
        return type(self)(self._data + other._data)
        
class R(P, Q):
    
    pass

def add(o1, o2):
    try:
        print(o1 + o2)
    except:
        print(traceback.format_exc())

t1 = T(1)
t1 += T(3)
print(t1)
'''
>>>  < T 1 >  self add
 < T 4 > 
'''

p1 = P(1)
add(p1, t1)
add(t1, p1)
'''
Traceback (most recent call last):
  File "jdoodle.py", line 34, in add
    print(o1 + o2)
TypeError: unsupported operand type(s) for +: 'P' and 'T'

>>>  < P 1 >  right add  < T 4 > 
 < P 5 > 
'''

q1 = Q(2)
add(q1, t1)
add(t1, q1)
'''
>>>  < Q 2 >  left add  < T 4 > 
 < Q 6 > 
Traceback (most recent call last):
  File "jdoodle.py", line 34, in add
    print(o1 + o2)
TypeError: unsupported operand type(s) for +: 'T' and 'Q'

'''

r1 = R(3)
add(r1, t1)
add(t1, r1)
add(r1, r1)
'''
>>>  < R 3 >  left add  < T 4 > 
 < R 7 > 
>>>  < R 3 >  right add  < T 4 > 
 < R 7 > 
>>>  < R 3 >  left add  < R 3 > 
 < R 6 > 
'''