#Dict comprehension: lap phuong cac so le

def odd_cubes(n):
    return {x : x**3 for x in range(1, n+1) if x % 2 != 0}

t = int(input("Nhap so test case = "))
for _ in range(t):
    n = int(input("Nhap so can xet = "))
    print(odd_cubes(n))