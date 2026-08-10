#Unpacking nang cao

def first_and_rest(lst):
    first, *rest = lst
    return first, rest

def last_and_rest(lst):
    *rest, last = lst
    return last, rest

def swap_ends(lst):
    first, *middle, last = lst
    return [last, *middle, first]

# Test
print(first_and_rest([1,2,3,4,5]))
print(last_and_rest([1,2,3,4,5]))
print(swap_ends([1,2,3,4,5]))
print(swap_ends([1,2]))