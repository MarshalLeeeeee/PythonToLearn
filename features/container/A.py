import sys
import traceback

class HashListNode(object):
    
    def __init__(self, key, value, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        if prev: prev.next = self
        if next: next.prev = self
        
    def __str__(self):
        return '< Node %s %s >' % (self.key, self.value)

class HashList(object):
    
    def __init__(self):
        self._head = HashListNode(None, None)
        self._tail = HashListNode(None, None)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._len = 0
        
    def append(self, k, v):
        HashListNode(k, v, self._tail.prev, self._tail)
        self._len += 1
        
    def delete_node(self, node):
        _prev = node.prev
        _next = node.next
        if _prev: _prev.next = _next
        if _next: _next.prev = _prev
        del node
        self._len -= 1
        
    def __len__(self):
        return self._len
        
    def __iter__(self):
        _node = self._head
        while True:
            if _node is None:
                break
            elif _node.key is None:
                _node = _node.next
            else:
                yield _node
                _node = _node.next
                
    def __reversed__(self):
        _node = self._tail
        while True:
            if _node is None:
                break
            elif _node.key is None:
                _node = _node.prev
            else:
                yield _node
                _node = _node.prev

class MyDict(object):
    
    MAX_HASH_SLOTS = 10000
    
    def __init__(self, k_type, v_type):
        self._k_type = k_type
        self._v_type = v_type
        self._hash_list = [None] * self.MAX_HASH_SLOTS
        
    def __getitem__(self, _key):
        print('>>> __getitem__', _key)
        _hash = hash(_key) % self.MAX_HASH_SLOTS
        if self._hash_list[_hash] is None:
            raise KeyError
        else:
            
            for _node in self._hash_list[_hash]:
                if _key == _node.key:
                    return _node.value
            raise KeyError
    
    def __setitem__(self, _key, _value):
        print('>>> __setitem__', _key, _value)
        if not isinstance(_key, self._k_type):
            raise TypeError('>>> Key is not an instance of type %s' % self._k_type)
        elif not isinstance(_value, self._v_type):
            raise TypeError('>>> Value is not an instance of type %s' % self._v_type)
        else:
            _hash = hash(_key) % self.MAX_HASH_SLOTS
            if self._hash_list[_hash] is None:
                self._hash_list[_hash] = HashList()
            for _node in self._hash_list[_hash]:
                if _key == _node.key:
                    _node.value = _value
                    break
            else:
                self._hash_list[_hash].append(_key, _value)

    def __delitem__(self, _key):
        print('>>> __delitem__', _key)
        _hash = hash(_key) % self.MAX_HASH_SLOTS
        if self._hash_list[_hash] is None:
            raise KeyError
        else:
            _node_to_delete = None
            for _node in self._hash_list[_hash]:
                if _key == _node.key:
                    _node_to_delete = _node
                    break
            if _node_to_delete:
                self._hash_list[_hash].delete_node(_node_to_delete)
                if not len(self._hash_list[_hash]):
                    self._hash_list[_hash] = None
            else:
                raise KeyError
                
    def __contains__(self, _key):
        print('>>> __contains__', _key)
        return _key in self._k_set


l = HashList()
l.append('test1', 1)
l.append('test2', 2)
l.append('test2', 2)
l.append('test3', 3)
_node_del = None
for _node in l:
    if _node.value == 1:
        _node_del = _node
    print(_node)
print('>>>> del value 1 node <<<<')
l.delete_node(_node_del)
for _node in reversed(l):
    print(_node)
'''
< Node test1 1 >
< Node test2 2 >
< Node test2 2 >
< Node test3 3 >
>>>> del value 1 node <<<<
< Node test3 3 >
< Node test2 2 >
< Node test2 2 >
'''
    
print('>>>>> test hash dict <<<<<')
d = MyDict(str, int)

def try_set(key, value):
    global d
    try:
        d[key] = value
        print('>>> try_set', key, d[key])
    except:
        print(traceback.format_exc())
    
def try_get(key):
    global d
    try:
        print('>>> try_get', key, d[key])
    except:
        print(traceback.format_exc())
        
def try_del(key):
    global d
    try:
        print('>>> try_del', key)
        del d[key]
    except:
        print(traceback.format_exc())
        
try_get(1)
try_set(1,1)
try_set('str1',1)
try_set('str2',2)
try_get('str1')
try_get('str2')
try_get('str3')
try_del('str1')
try_get('str1')
try_get('str2')
try_get('str3')
print('str3' in d)
'''
('>>> __getitem__', 1)
Traceback (most recent call last):
  File "jdoodle.py", line 138, in try_get
    print('>>> try_get', key, d[key])
  File "jdoodle.py", line 65, in __getitem__
    raise KeyError
KeyError

('>>> __setitem__', 1, 1)
Traceback (most recent call last):
  File "jdoodle.py", line 130, in try_set
    d[key] = value
  File "jdoodle.py", line 76, in __setitem__
    raise TypeError('>>> Key is not an instance of type %s' % self._k_type)
TypeError: >>> Key is not an instance of type <type 'str'>

('>>> __setitem__', 'str1', 1)
('>>> __getitem__', 'str1')
('>>> try_set', 'str1', 1)
('>>> __setitem__', 'str2', 2)
('>>> __getitem__', 'str2')
('>>> try_set', 'str2', 2)
('>>> __getitem__', 'str1')
('>>> try_get', 'str1', 1)
('>>> __getitem__', 'str2')
('>>> try_get', 'str2', 2)
('>>> __getitem__', 'str3')
Traceback (most recent call last):
  File "jdoodle.py", line 138, in try_get
    print('>>> try_get', key, d[key])
  File "jdoodle.py", line 65, in __getitem__
    raise KeyError
KeyError

('>>> try_del', 'str1')
('>>> __delitem__', 'str1')
('>>> __getitem__', 'str1')
Traceback (most recent call last):
  File "jdoodle.py", line 138, in try_get
    print('>>> try_get', key, d[key])
  File "jdoodle.py", line 65, in __getitem__
    raise KeyError
KeyError

('>>> __getitem__', 'str2')
('>>> try_get', 'str2', 2)
('>>> __getitem__', 'str3')
Traceback (most recent call last):
  File "jdoodle.py", line 138, in try_get
    print('>>> try_get', key, d[key])
  File "jdoodle.py", line 65, in __getitem__
    raise KeyError
KeyError

False
'''