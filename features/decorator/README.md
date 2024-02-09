# Decorator
[reference](https://peps.python.org/pep-0318/)

## Motivation:
Wrapping the transformation of a function or method. Make it encapsulated and more readable. Although metaclass can provide sufficient ability, we can introduce an easier notation. 

```
def foo(cls):
    pass
foo = synchronized(lock)(foo)
foo = classmethod(foo)

<=>

@classmethod
@synchronized(lock)
def foo(cls):
    pass
```

## Implementation of decorator:

### Function decorator:
Basicly, what after @ as a deco which wraps one function as the input to a new callable object which is actually executed. __A.py__

### Class decorator:
The class decorators can format the way of getting callables like a factor, combined with function decorators. Besides, with the representation of class, methods can be further reusable due to inheritance. __B.py__

Class decorators with parameters can be designed in a two stage schema (two instances created) as well as a one class schema (one instance created). __C.py__

The class decorators can modify class attribute when functions are declared while the function decorators do not execute until runtime. __D.py__