#Itertools.combinations + itertools.permutations

import itertools

def all_subsets(lst, r):
    return list(itertools.combinations(lst, r))

def all_arrangements(lst):
    return list(itertools.permutations(lst))

print(all_subsets([1,2,3,4], 2))

print(all_subsets([1,2,3], 3))

print(all_arrangements([1,2,3]))
