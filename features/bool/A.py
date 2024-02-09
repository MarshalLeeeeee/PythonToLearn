class O(object):

    pass

class T(O):

    def __len__(self):
        print('>>> __len__')
        return 0

class P(T):

    def __bool__(self):
        print('>>> __bool__')
        return False

o = O()
if o:
    print('o1')
else:
    print('o0')
t = T()
if t:
    print('t1')
else:
    print('t0')
p = P()
if p:
    print('p1')
else:
    print('p0')

'''
Python2
o1
>>> __len__
t0
>>> __len__
p0

Python3
o1
>>> __len__
t0
>>> __bool__
p0
'''