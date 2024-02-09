class T(object):

    def __repr__(self):
        return '__T__repr__'
    
    def __str__(self):
        return '__T__str__'
        
    def __format__(self, format_spec):
        print '>>>> format_spec ', format_spec
        return '__T__format__'

def show_t(t):
    print('=======================')
    print(t)
    print('%s' % t)
    print('--- {0:2d} ---'.format(t))
    print(str(t))
    print(repr(t))
    print('=======================')

t = T()
show_t(t)
'''
=======================
__T__str__
__T__str__
>>>> format_spec  2d
--- __T__format__ ---
__T__str__
__T__repr__
=======================
'''