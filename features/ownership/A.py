class T(object):

    d = {}

    def local_assign(self, _d):
        self.d = _d

    def local_update(self, _d):
        self.d.update(_d)

    @classmethod
    def cls_assign(cls, _d):
        cls.d = _d

def print_info(t):
    print(t.d)
    print(T.d)
    print(id(t.d))
    print(id(T.d))
    print()

t1 = T()
print_info(t1)
'''
Instance member has the same reference as class member when created
{}
{}
11569536
11569536
'''

t1.cls_assign({2:2})
print_info(t1)
'''
If class member refer to a new object, the instance member follows. This happens as long as they refer to the same object
{2: 2}
{2: 2}
13392632
13392632
'''

t1.local_assign({1:1})
print_info(t1)
'''
Once the instance member refer to a new object, it deviates from class member
{1: 1}
{2: 2}
11569536
13392632
'''

t1.local_assign({3:3})
print_info(t1)
'''
Once the instance member refer to a new object, it deviates from class member, however the instance changed, the class member remains.
{3: 3}
{2: 2}
10047984
13392632
'''

t2 = T()
print_info(t2)
'''
Instance member has the same reference as class member when created
{2: 2}
{2: 2}
13392632
13392632
'''

t2.local_update({4:4})
print_info(t2)
'''
If the instance operate on the same object, it stills remains same with class member
{2: 2, 4: 4}
{2: 2, 4: 4}
13392632
13392632
'''

t2.local_assign({5:5})
print_info(t2)
'''
{5: 5}
{2: 2, 4: 4}
11569536
13392632
'''