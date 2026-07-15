#Generator tong tich luy

def running_sum(iterable):
    s = 0
    for x in iterable:
        s += x
        yield s

print(list(running_sum([1, 2, 3, 4])))
print(list(running_sum([5])))
print(list(running_sum([])))