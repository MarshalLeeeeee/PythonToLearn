import sys

class T(object):
    
    def __init__(self, data):
        self.data = data

    def __del__(self):
        print '>>>> __del__'
        super()
        
t = T(1)
p = t
q = t
del p
print sys.getrefcount(t)
del q
print sys.getrefcount(t)
del t
print sys.getrefcount(t)

'''
3 # 1 count higher than real conut, due to reference passed as paramter
2 # 1 count higher than real conut, due to reference passed as paramter
>>>> __del__

Traceback (most recent call last):
  File "jdoodle.py", line 20, in <module>
    print sys.getrefcount(t)
NameError: name 't' is not defined
'''