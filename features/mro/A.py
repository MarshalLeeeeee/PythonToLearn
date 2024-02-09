class T:
    v = 0
    
class T1(T):
    pass

class T2(T):
    v = 2
    
class T3(T1, T2):
    pass

class T4(T2, T1):
    pass

print T3.v # 0
print T4.v # 2