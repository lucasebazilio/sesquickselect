# sesquickselect
This repository shows the implementation of the sesquickselect algorithm, a variant of the quickselect algorithm.
Sesquickselect aims at reducing cache misses and thus improving running time of the standard quickselect algorithm.
To this end, sesquickselect will randomly pick two pivots for each recursive stage, use one of them or both to partition the current subarray and continue recursively in the part that contains the sought element.

Papers:
1. Sebastian Wild. Dual-pivot and beyond: The potential of multiway partitioning in quicksort. Information Technology 60(3): 173–177, 2018. Available from: https://www.wild-inter.net/publications/wild-2018b.
pdf
2. Conrado Martínez, Markus Nebel and Sebastian Wild. Sesquickselect:
One and a half pivots for cache-efficient selection. In Marni Mishna,
J. Ian Munro, editors, Proc. of the 16th Workshop on Analytic Algorithmics and Combinatorics, ANALCO 2019, San Diego, CA, USA,
January 6, 2019. Pages 54–66, SIAM, 2019. Available from: https:
//epubs.siam.org/doi/10.1137/1.9781611975505.6. On-line full version available from https://arxiv.org/abs/1810.12322
3. Conrado Martínez, Daniel Panario and Alfredo Viola. Adaptive sampling
strategies for quickselect. ACM Transactions on Algorithms 6(3), pages
53:1–53:45, 2910. Available from: https://dl.acm.org/doi/10.1145/
1798596.1798606
