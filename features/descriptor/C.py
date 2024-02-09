class MYProperty(object):
    
    def __init__(self, getter=None, setter=None, deleter=None):
        self._getter = getter
        self._setter = setter
        self._deleter = deleter
    
    def __get__(self, instance, owner=None):
        if instance is None:
            print '>>>> instance is None'
        elif not callable(self._getter):
            print '>>>> getter is not callable'
        else:
            return self._getter(instance)
    
    def __set__(self, instance, value):
        if instance is None:
            print '>>>> instance is None'
        elif not callable(self._setter):
            print '>>>> setter is not callable'
        else:
            self._setter(instance, value)
    
    def __delete__(self, instance):
        if instance is None:
            print '>>>> instance is None'
        elif not callable(self._setter):
            print '>>>> deleter is not callable'
        else:
            self._deleter(instance)
    
    def my_getter(self, getter):
        print '>>> my getter', self._getter, self._setter, self._deleter
        return type(self)(getter, self._setter, self._deleter)
    
    def my_setter(self, setter):
        print '>>> my setter', self._getter, self._setter, self._deleter
        return type(self)(self._getter, setter, self._deleter)
    
    def my_deleter(self, deleter):
        print '>>> my deleter', self._getter, self._setter, self._deleter
        return type(self)(self._getter, self._setter, deleter)
        

class T(object):
    
    def __init__(self):
        self._succ = False

    @MYProperty   
    def succ_or_not(self):
        return 'succ or not getter? ', self._succ
        
    @succ_or_not.my_setter
    def succ_or_not(self, value):
        print 'succ or not setter ', value
        self._succ = value
        
    @succ_or_not.my_deleter
    def succ_or_not(self):
        print 'succ or not deleter '
        self._succ = False
'''
>>> my setter <function succ_or_not at 0x7fa016fdfbd0> None None
>>> my deleter <function succ_or_not at 0x7fa016fdfbd0> <function succ_or_not at 0x7fa016fdfc50> None
'''

t1 = T()
t2 = T()
print t1
print t1.succ_or_not
print '\n'
print t2
t2.succ_or_not = True
print t2.succ_or_not
del t2.succ_or_not
print t2.succ_or_not
'''
<__main__.T object at 0x7fa016fe3c10>
('succ or not getter? ', False)


<__main__.T object at 0x7fa016fe3c50>
succ or not setter  True
('succ or not getter? ', True)
succ or not deleter 
('succ or not getter? ', False)
'''
