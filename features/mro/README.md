# MRO

[ref1](https://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python)

[ref2](https://www.python.org/download/releases/2.3/mro/)

## Old style class

Old-style class MRO: dfs search for the target attribute. __A.py__

## New style class

New-style class (C3)MRO basicly solves the confusion of result derived from inheritence sequence. Lets suppose C is the inheritence of B1, B2, BN, the linearization of C is 

```
L(C(B1B2...BN)) = C + merge(L(B1), L(B2), ..., L(BN), B1B2...BN)
L(object) = object
```

The merge function works as follows. Travers the seq from left to right to see if the head of some seq is not in the tail of any other seq. If find one, return this node, remove the node, and do merge for the rest recursively.

```
>>> O = object
>>> class F(O): pass
>>> class E(O): pass
>>> class D(O): pass
>>> class C(D,F): pass
>>> class B(D,E): pass
>>> class A(B,C): pass

L(O) = O
L(F) = FO
L(E) = EO
L(D) = DO
L(C) = C + merge(L(D), L(F), DF) = C + merge(DO, FO, DF) = CD + merge(O, FO, F) = CDF + merge(O, O) = CDFO
L(B) = B + merge(L(D), L(E), DE) = B + merge(DO, EO, DE) = BDEO
L(A) = A + merge(L(B), L(C), B, C) = A + merge(BDEO, CDFO, BC) = AB + merge(DEO, CDFO, C) = AB + merge(DEO, CDFO, C) = ABC + merge(DEO, DFO) = ABCD + merge(EO, FO) = ABCDEFO
```

If this procedure fails, python will raise TypeError: Error when calling the metaclass bases. Cannot create a consistent method resolution. __B.py__

Can this happen for new style class? Lets prove some lemmas.

Lemma 1: A valid linearization will not contain duplicated class node. 
```
Prove by induction: suppose the previous linearization do not contain duplicated nodes
In equation:
    L(C(B1B2...BN)) = C + merge(L(B1), L(B2), ..., L(BN), B1B2...BN)

The duplication can only happen when C is in L(Bx)
However, circle inheritance is not supported by the python context, therefore will not happen.
```

Lemma 2: The relative order of linearization of the base calss is reserved in the merged result of a valid linearization.
```
We suppose the linearization of C is valid
In equation:
    L(C(B1B2...BN)) = C + merge(L(B1), L(B2), ..., L(BN), B1B2...BN)
the merge procedure will halt.

Suppose in L(Bx) we have CxD, but we have DxC in L(C), 
then in the merge step where we get D should look like
merge(..., Dxxxxx, ..., xxCxDx, ...)

Therefore, this merge step is invalid, because D is in the tail of xxCDx.
```

However, even all using new-style class, bad merge can still happen. Because the final seq is defined by the user which is the explicit seq of the base classes which might conflicts the relative order of all other valid linearization. __C.py__
```
class F(object): pass
class E(F): pass
class G(F, E): pass

L(G) = G + merge(L(F), L(E), FE)
     = G + merge(FO, EFO, FE) // stuck
```
