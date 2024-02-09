class T(object):

    def __enter__(self):
        print('T__enter__')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('T__exit__', exc_type, exc_value, traceback)
        return True

t = T()
with t as tt:
    print('>>> t', t)
    print('>>> tt', tt)

'''
T__enter__
>>> t <__main__.T object at 0xf5f950>
>>> tt <__main__.T object at 0xf5f950>
T__exit__ None None None
'''
