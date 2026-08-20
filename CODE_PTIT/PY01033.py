# Một cặp số nguyên dương (a,b) được gọi là nguyên tố cùng nhau nếu a và b có ước chung lớn nhất bằng 1. Một bộ ba số (a, b, c) được gọi là bộ ba nguyên tố cùng nhau nếu a < b < c và các cặp (a,b), (b,c), (a,c) đều nguyên tố cùng nhau.

# Cho hai số nguyên dương L và R (10 < L < R < 200). Hãy viết chương trình liệt kê các bộ ba số nguyên tố cùng nhau trong đoạn [L, R].

# Input

# Chỉ có 2 số L và R

# Output

# Ghi ra các bộ ba số nguyên tố cùng nhau, mỗi bộ ba trên một dòng theo định dạng như trong ví dụ.

# Các bộ ba được liệt kê theo thứ tự từ điển tăng dần.

# Ví dụ



# Input

# Output

# 15 20

	
# (15, 16, 17)


# (15, 16, 19)


# (15, 17, 19)


# (16, 17, 19)


# (17, 18, 19)


# (17, 19, 20)  

from math import gcd

l, r = map(int, input().split())

def GCD(a : int, b : int, c : int) -> bool:
    return (gcd(a, b) == 1 and gcd(b, c) == 1 and gcd(a, c) == 1)


for i in range(l, r - 2):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if GCD(i, j, k):
                print(f"({i}, {j}, {k})")