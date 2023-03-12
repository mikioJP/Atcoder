import sys
sys.setrecursionlimit(10**6)
import numpy as np
import bisect
from scipy.sparse.csgraph import floyd_warshall 
from heapq import heappop, heappush
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations,combinations_with_replacement,product
