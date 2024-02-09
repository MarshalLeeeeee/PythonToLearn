# Representation

```__repr__``` : called by ```repr()``` method, return a string. The string should contain sufficient information-rich and unambiguous. Mostly used for debugging.What's more, iIf we print the dict, the key and value are shown in repr.

```__str__``` : called by ```str()``` or any implicit string-conversion. The string is intended for user-display. If not defined, depreciated to ```__repr__```.


```__format__``` : called by format(). The string is intended to be variated according to the input format_spec and will be filled into the brackets.