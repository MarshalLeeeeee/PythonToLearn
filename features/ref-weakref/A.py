import sys

class A(object):

    def __del__(self):
        print '>>> __del__ A'

class B(object):

    def __del__(self):
        print '>>> __del__ B'

a = A()
b = B()
a.b = b
b.a = a
print(sys.getrefcount(a))
print(sys.getrefcount(b))
'''
3 # one more count due to method paramter
3 # one more count due to method paramter
# no destructor called
'''