_s = '啊'
_e = _s.encode('utf-8')
print(_s)
print(_e)
_ee = list(_e)
_ee[-1] += 1
_ee = bytes(_ee)
print(str(_ee, encoding='utf-8'))

'''
啊
b'\xe5\x95\x8a'
啋
'''