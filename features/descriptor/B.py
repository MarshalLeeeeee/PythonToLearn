def validate_type(_type):
    def cls_deco(cls):
        cls.TYPE = _type
        return cls
    return cls_deco

class ValidatorBase(object):
    
    TYPE = None
    
    def __init__(self):
        self._v = None
    
    def __get__(self, instance, owner=None):
        print '>>>>>>> getter succ %s' % self._v, instance
        return self._v
        
    def __set__(self, instance, value):
        if value is not None and not isinstance(value, self.TYPE):
            print '>>>>>>> setter failed because %s is not type %s' % (value, self.TYPE)
        else:
            self._v = value
            print '>>>>>>> setter succ %s' % value
        
    def __delete__(self, instance):
        del self._v
        
@validate_type(int)
class ValidatorInt(ValidatorBase):
    
    pass

class T(object):
    v_int = ValidatorInt()
    
t = T()
t.v_int = 2.0
t.v_int = 'str'
t.v_int = None
t.v_int = 1
t.v_int
t2 = T()
t2.v_int
'''
>>>>>>> setter failed because 2.0 is not type <type 'int'>
>>>>>>> setter failed because str is not type <type 'int'>
>>>>>>> setter succ None
>>>>>>> setter succ 1
>>>>>>> getter succ 1 <__main__.T object at 0x7f5b70c6eb50>
>>>>>>> getter succ 1 <__main__.T object at 0x7f5b70c6eb90>
'''
