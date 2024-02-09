# Static variables:

[ref](https://wiki.python.org/moin/UsingSlots)

Python class provides the ability of adding dynamic variables, but can cause a defection in memory and variable checkup (obvious when large amount of instances are created)

```__slots__``` makes the variable static, optimizes the memory and speeds up checkup by pre-defining variable names. By default, ```__slots__``` will remove ```__dict__``` (make it not dynamic variable) and ```__weakref__``` (make it unable to be weakrefed). But we can enable them by putting them back to ```__slot__```. __A.py__

```__slots__``` should be better designed at immutable. Making it mutable leads no benifits since this class attribute seems to make effect during declaration. __B.py__

Inheritence will not have static variables, i.e. ```__dict__``` and ```__weakref__``` is in dir() __C.py__
