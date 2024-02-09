# Descriptors:
[ref1](https://www.datacamp.com/tutorial/python-descriptors)

[ref2](https://www.topcoder.com/thrive/articles/use-of-descriptors-in-python)

Descriptor methods only work when the descriptor is an instance of a class attribute. Can check it in ref [ref3](https://stackoverflow.com/questions/17630931/why-get-method-is-not-called-for-instance-attribute)

```__get__```: return value when the descriptor itself is visited. The intance of the exact object, owner is the corresponding class. Owner parameter should better be given None as the default value to compatible Python3.

```__set__```: is called when the descriptor itself is assigned by a assignment statement.

```__delete__```: is called whent the descriptor is deleted by del operator.

## Implementation and usage

Descriptors can be used to extend the read and write behavior of itself. It is helpful in data write validation. __B.py__

Descriptor can be used to implement property. Still, classmethod and staticmethod is a descriptor which implements ```__get__``` only. (classmethod take use of owner parameterm while staticmethod omit instance and owner). __C.py__
