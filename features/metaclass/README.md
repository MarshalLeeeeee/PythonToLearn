# Metaclass

Everything is object in python, therefore, everything is an instance of a "Class". The class of a class is what we called metaclass.

The metaclass should be be a subclass of type whose ```__new__(cls, name, bases, attrs)``` should be usually overriden. This method of metaclass is called right after the class is declared (we can simply think the declaration of class as the same behavior as we declare the instance of a class).

```__new__``` is a method that every class has. It returns the instantiated object which calls ```__init__``` right after (if the object returned is really an instance of the class). __A.py__