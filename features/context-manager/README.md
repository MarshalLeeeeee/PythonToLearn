# Context manager:

Implement with the with-statement. 

```__enter__``` is called by the instance right after with. The return value is stored after as.

```__exit__``` should not reraise exceptions. If not exception happens, the paramters are all None. The return value only matters when the parameter is not None. In this case, return True to swallow the exception (meaning the exception is gracefully handled); return False to propagate the exception.
