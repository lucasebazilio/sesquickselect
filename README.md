# sesquickselect
This repository shows the implementation of the sesquickselect algorithm, a variant of the quickselect algorithm
Sesquickselect aims at reducing cache misses and thus improve running time of the standard quickselect algorithm.
To this end, sesquickselect will randomly pick two pivots for each recursive stage, use one of them or both to partition the current subarray and continue recursively in the part that contains the sought element.
