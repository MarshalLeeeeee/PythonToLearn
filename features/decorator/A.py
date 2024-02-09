def print_hello(func):
    def wrapper():
        print('hello')
        return func()
    return wrapper

def test_func_1_raw():
    print('this is test func 1')

@print_hello
def test_func_1():
    print('this is test func 1')
    
test_func_1_raw = print_hello(test_func_1_raw)
test_func_1_raw()
# hello
# this is test func 1
test_func_1()
# hello
# this is test func 1

def print_any(prefix):
    def deco(func):
        def wrapper(txt):
            print(prefix)
            return func(txt)
        return wrapper
    return deco
    
def test_func_2_raw(txt):
    print(txt)

@print_any('prefix')
def test_func_2(txt):
    print(txt)

test_func_2_raw = print_any('prefix')(test_func_2_raw)
test_func_2_raw('body')
# prefix
# body
test_func_2('body')
# prefix
# body
