import sys
import weakref

class A(object):

    def __del__(self):
        print '>>> __del__ A'

class B(object):

    def __del__(self):
        print '>>> __del__ B'

a = A()
b = B()
a.b = weakref.ref(b)
b.a = weakref.ref(a)
print(sys.getrefcount(a))
print(sys.getrefcount(b))

class T(object):

    def __del__(self):
        print '>>> __del__ T'

t = T()
tt = weakref.ref(t)
print(tt)
print(tt())
print(sys.getrefcount(tt()))
tt().v = 1
print(t.v)
del t
print(tt)
print(tt())

'''
2 # one more count due to method paramter, weakref does not increase the reference count
2 # one more count due to method paramter, weakref does not increase the reference count

<weakref at 00000000034388B8; to 'T' at 000000000343A548>
<__main__.T object at 0x000000000343A548> # get temp reference from () operator
2 # one more count due to method paramter, weakref does not increase the reference count

1 # use temp reference from () operator to modify reference attribute

# After t is destroyed
<weakref at 00000000038F8958; dead>
None # when referenced object is destroyed get None

# now destructors are called
>>> __del__ B
>>> __del__ A
'''