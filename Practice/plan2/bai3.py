#Gop 2 dict, cong gia tri neu trung lap key

from collections import Counter

def wordFreq(s):
    x = s.split()
    return Counter(x)


def mergeSum(a, b):
    d1 = wordFreq(a)
    d2 = wordFreq(b)

    res = dict(d1)

    for key, value in d2.items():
        if key in res:
            res[key] += value
        else:
            res[key] = value
    return res

a = input()
b = input()

ans = mergeSum(a, b)
print(ans)