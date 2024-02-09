# Container:

```__getitem__``` (raise KeyError for map container, raise IndexError for seq container, raise TypeError for type mis-match), ```__setitem__```, ```__delitem__``` are called when [] operator is used to read or write data in the container or del operator is used to remove data from the container.

```__len__``` is called to return the exact length of the container. ```__length_hint__``` is called to return inaccurate length but with better time efficiency.

```__iter__``` yield objects for iterator use. ```__reversed__``` yields (or just return the full iterable object) reversely. If not implemented, the reverse algorithm will fallback to use ```__len__``` and ```__getitem__``` (which require the object should be an instance of a sequence type).

```__contains__``` is called when in operator is used. ```__getitem__``` is not is default fallback when ```__contains__``` is not implemented, instead ```__iter__``` is used for a O(n) lookup. Therefore, if ```__iter__``` is not defined for a custom container, in operator might fail to perform correctly.
