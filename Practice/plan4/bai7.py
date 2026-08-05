#Itertools.chain: gop nhieu iterable

import itertools
import heapq

def chain(*lists):
    return list(itertools.chain(*lists))

def merge_sorted(*lists):
    return list(heapq.merge(*lists))

print(merge_sorted([1,4,7], [2,5,8], [3,6,9]))
print(chain([1,4,7], [2,5,8], [3,6,9]))

print(merge_sorted([1,3], [2,4], []))
print(chain([1,3], [2,4], []))