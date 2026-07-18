#itertools.groupby: loai theo loai

def group_by_parity(nums):
    return {
        "even": [x for x in nums if x % 2 == 0],
        "odd": [x for x in nums if x % 2 != 0]
    }

print(group_by_parity([1,2,3,4,5,6]))
print(group_by_parity([2,4]))