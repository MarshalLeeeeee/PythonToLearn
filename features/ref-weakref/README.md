# Reference & Weakref:

Reference to an object (or a piece of data in memory) can be approximated as create a new name. Reference count is thus the count of names of the object. An object is dustructed when the reference count decrease to zero. (See Section Special methods / Destructor)

This design can cause some problems, like reference circle. __A.py__

To avoid this, we can use weakref. The weakref object will not increase the reference count. By () operator, we get a temp reference if the object is alive or None if the object is dead. __B.py__

