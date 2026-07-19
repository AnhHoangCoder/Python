#heapq: K phan tu lon nhat

import heapq

def top_k(nums, k):
    return heapq.nlargest(k, nums)

t = int(input("Nhap so test case: "))
for _ in range(t):
    s = input("Nhap so phan tu trong mang: ")
    k = int(input("Nhap so k = "))

    nums = list(map(int, s.split()))
    print(top_k(nums, k))
