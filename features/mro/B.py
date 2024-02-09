class X: pass
class Y: pass
class Z: pass
class W(X,Y): pass
class T(Y,X): pass
class U(W,T,object): pass

print U.__mro__

'''
Traceback (most recent call last):
  File "jdoodle.py", line 6, in <module>
    class U(W,T,object): pass
TypeError: Error when calling the metaclass bases
    Cannot create a consistent method resolution
order (MRO) for bases X, Y
'''