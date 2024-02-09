class T(object):

    def __bytes__(self):
        return '啊'.encode()

t = T()
print(bytes(t))
print(str(bytes(t), encoding='utf-8'))
'''
b'\xe5\x95\x8a'
啊
'''