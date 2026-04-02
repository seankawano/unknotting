# Improving u(K) Lower Bounds

A theorem of McCoy [1] states $u(K) = 1$ if and only if $K$ has an unknotting crossing in every alternating diagram. Mark Brittenham used this result to improve the $u(K)$ lower bound for prime knots up to 12 crossings [2]. We attempted to apply this same verificiation up to 13 crossings in the Knotinfo database. 

| File | |
|------------|-----|
| main.ipynb | main notebook that includes the code for my computation |
| alt.py | contains relavent code for the computations from main.ipynb in a .py file |
| knotinfo.csv | original data from knotinfo [3] accessed 4/1/2026 |
| updated_u(K)_values.csv | output of main.ipynb / alt.py |

### References
[1] Duncan McCoy,
Alternating knots with unknotting number one,
Advances in Mathematics,
Volume 305,
2017,
Pages 757-802,
ISSN 0001-8708,
https://doi.org/10.1016/j.aim.2016.09.033.
(https://www.sciencedirect.com/science/article/pii/S0001870816312944)

[2] (https://knotinfo.org/descriptions/brittenham-letter.html)

[3] C. Livingston and A. H. Moore, KnotInfo: Table of Knot Invariants, knotinfo.org, April 1, 2026
