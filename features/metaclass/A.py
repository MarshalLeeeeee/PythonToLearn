class TMeta(type):
    
    def __new__(cls, name, bases, attrs):
        print('>>>> Tmeta new: ', name, bases, attrs)
        return super(TMeta, cls).__new__(cls, name+'_MY', bases, attrs)


class T(object):
    
    __metaclass__ = TMeta
    
    def __new__(cls, data):
        print('>>>> T new: ', data)
        cls_instance = super(T, cls).__new__(cls, data)
        print('>>>>> cls instance', cls_instance)
        print('>>>>> cls instance', type(cls_instance))
        return cls_instance
        
    def __init__(self, data):
        print('>>>> T init instance', self)
        print('>>>> T init instance', type(self))
        super(T, self).__init__(self)
        self.data = data
        print('>>>> T init', self.data)
        
    def __str__(self):
        return '<T> ' + str(self.data)
        
class TT(T):
    pass
        
class P(object):
    
    def __new__(cls, data):
        print('>>>> P new: ', data)
        return int(data)
        
    def __init__(cls, data):
        print('>>>> P init instance', self)
        print('>>>> P init instance', type(self))
        super(P, self).__init__(self)
        self.data = data
        print('>>>> P init', self.data)
        

t = T(1)
print(t)
print(type(t))
print(type(T))
'''
# for __new__(cls, name, bases, attrs)
# name is the name of the class
# bases is the list of direct parent classes
# attrs is the dict of the spec(overriden) attributes of the class
('>>>> Tmeta new: ', 'T', (<type 'object'>,), {'__module__': '__main__', '__metaclass__': <class '__main__.TMeta'>, '__new__': <function __new__ at 0x7efe62835750>, '__init__': <function __init__ at 0x7efe628357d0>, '__str__': <function __str__ at 0x7efe62835850>})
('>>>> Tmeta new: ', 'TT', (<class '__main__.T_MY'>,), {'__module__': '__main__'})

# new is firstly called
('>>>> T new: ', 1)
# return the instantiated object
('>>>>> cls instance', <__main__.T_MY object at 0x7efe62839c10>)
('>>>>> cls instance', <class '__main__.T_MY'>)
# the self in init is the same as what new returns
('>>>> T init instance', <__main__.T_MY object at 0x7efe62839c10>)
('>>>> T init instance', <class '__main__.T_MY'>)
('>>>> T init', 1)
<T> 1
<class '__main__.T_MY'> # the class name
<class '__main__.TMeta'> # the metaclass
'''

p = P(1)
print(p)
print(type(p))
print(type(P))
'''
('>>>> P new: ', 1)
# if the return object of new is not an instance of the class, init will not be called
1
<type 'int'>
<type 'type'> # the default metaclass is type
'''    
