class T(object):
    
    def __init__(self):
        print('>>>> T__init__')
        self._v = 0
    
    def __get__(self, instance, owner=None):
        print('>>>> T__get__', instance, owner, self._v)
        return self._v
        
    def __set__(self, instance, value):
        print('>>>> T__set__', instance, value)
        self._v = value
        
    def __delete__(self, instance):
        print('>>>> T__delete__', instance)
        del self._v
        
    def __getattr__(self, name):
        print('>>>> T__getattr__', name)
        
    def __setattr__(self, name, value):
        print('>>>> T__setattr__', name, value)
        return super(T, self).__setattr__(name, value)
        
    def __delattr__(self, name):
        print('>>>> T__delattr__', name)
        return super(T, self).__delattr__(name)
        
    def __del__(self):
        print('>>>> T__del__')

class P(object):
    t = T()
    
    def __init__(self):
        self.t = 0

    def __getattr__(self, name):
        print('>>>> P__getattr__', name)
        
    def __setattr__(self, name, value):
        print('>>>> P__setattr__', name, value)
        return super(P, self).__setattr__(name, value)
        
    def __delattr__(self, name):
        print('>>>> P__delattr__', name)
        return super(P, self).__delattr__(name)

    def __del__(self):
        print('>>>> P__del__')

    def __str__(self):
        return ' < P instance %d > ' % id(self)


'''
>>>> T__init__
>>>> T__setattr__ _v 0
'''

print('\n')
t = T()
t = 1
t = T()
del t
print('\n')
'''
# the descriptor methods can only make effect when it is a class attribute
>>>> T__init__
>>>> T__setattr__ _v 0
>>>> T__del__
>>>> T__init__
>>>> T__setattr__ _v 0
>>>> T__del__
'''

print('1---')
p = P()
print('2---')
p.t = 1
print('3---')
p.t
print('4---')
P.t
print('5---')
del p.t
print('6---')
p.t
print('7---')
p.t = 2
print('8---')
P.t
print('9---')
del p
'''
1---
>>>> P__setattr__ t 0 # P's attribute setter is called
>>>> T__set__  < P instance 10545776 >  0 # T's descriptor setter is called
>>>> T__setattr__ _v 0 # T's attribute setter is called
2---
>>>> P__setattr__ t 1 # P's attribute setter is called
>>>> T__set__  < P instance 10545776 >  1 # T's descriptor setter is called
>>>> T__setattr__ _v 1 # T's attribute setter is called
3---
>>>> T__get__  < P instance 10545776 >  <class '__main__.P'> 1 # T's descriptor getter is called
4---
>>>> T__get__ None <class '__main__.P'> 1 # T's descriptor getter is called, when called by class, instance is None
5---
>>>> P__delattr__ t # P's attribute deleter is called
>>>> T__delete__  < P instance 10545776 >  # T's descriptor deleter is called
>>>> T__delattr__ _v # T's attribute deleter is called
6---
>>>> T__getattr__ _v # T's fail lookup getter is called in print
>>>> T__get__  < P instance 10545776 >  <class '__main__.P'> None # T's descriptor getter is called
>>>> T__getattr__ _v # T's fail lookup getter is called in return
7---
>>>> P__setattr__ t 2 # P's attribute setter is called
>>>> T__set__  < P instance 10545776 >  2 # T's descriptor setter is called
>>>> T__setattr__ _v 2 # T's attribute setter is called
8---
>>>> T__get__ None <class '__main__.P'> 2 # T's descriptor getter is called by class
9---
>>>> P__del__ # p is deleted, but t is not????
'''