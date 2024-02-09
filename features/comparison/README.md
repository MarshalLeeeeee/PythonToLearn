# Comparison

## Rich comparison:
```__eq__```                                   == operation, own reflection

```__ne__```                                   != operation, own reflection

```__gt__``` and ```__lt__```                  > and < operation, each other's reflection

```__ge__``` and ```__le__```                >= and <= operation, each other's reflection

Reflection means the equal operator when the operants are swapped, therefore when ```__gt__``` is implemented and ```__lt__``` is not, the < operation will use implicitly swap the operants and use ```__gt__``` instead.


## Base comparison: 
```__cmp__```, ```__rcmp__``` used when the rich comparison and its reflection are both not implemented. (removed in Python3)

## Other
By the decorator - functools.total_ordering, we only need to define ```__eq__``` and any one of ```__gt__``` and ```__lt__``` and ```__ge__``` and ```__le__```