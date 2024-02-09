# Hash

```__hash__``` : called by hash() which is implicitly used in collections like set, frozenset, dict. 

This method returns an integer and must return equal results for equal objects. This should be guaranteed by developer. Still, mutability can cause unexpected bugs.