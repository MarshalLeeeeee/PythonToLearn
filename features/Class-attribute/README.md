# Class Attribute

## Common functions

```__getattr__``` is called when normal lookup fails. I.e., if the attribute is in the dir of the object, this method will not be called. object class does not have ```__getattr__``` method, so super is not reliable.

```__setattr__``` is called for any class attribute assignment (cls.attr = xxx). The default assignment behavior depends on whether the class used static or dynamic variables which might raise AttributeException.

```__delattr__``` is called for any class attribute deletion (del cls.attr). The default deletion behavior depends on whether the class has the attribute which might raise AttributeException.

__A.py__

## Python3 Exclusive

```__getattribute__``` (added in python3) is called for any class attribute lookup (cls.attr).

__B.py__
