# Steklov problem on hypersurfaces of revolution: numerical experiment

We are interested in the Steklov problem on hypersurfaces of revolution in the Euclidean space. 
While investigating it, we discovered a strange phenomenon. 
Some eigenvalues have a finite crtical length associated with, while others have got an infinite critical length.

We were able to prove mathematically that infinitely many eigenvalues have a finite critical lentgh, 
however we were **not** able to quantified how many eigenvalues have an infinite critical length associated with.

There exists an algorithm, called "extension process", which gives the sharp upper bound $B_n^k(L)$ for the $k$th eigenvalue, 
given the meridian length $L$ of the hypersurface and its dimension $n$. We used this algorithm to create four different programs,
which allows us to check what happen to "high" eigenvalues. We were able to check roughly to the $120 000$th eigenvalue.

These programs support the following conjecture:

**Conjecture**. Given $n \ge 3$, there exist finitely many $k \in \mathbb{N}$ such that the $k$th eigenvalue has an infinite critical length associated with.
