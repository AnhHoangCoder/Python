#Quicksort viết theo phong cách python

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)

t = int(input("Nhap so test case: "))
for _ in range(t):
    s = input("Nhap cac phan tu: ")
    arr = list(map(int, s.split()))
    print(quickSort(arr))