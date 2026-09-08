# Cho dãy số A[] có n phần tử là các số nguyên dương khác nhau, giá trị không quá 100. Hãy liệt kê các cặp số nguyên tố cùng nhau xuất hiện trong dãy theo thứ tự tăng dần, mỗi cặp số in trên một dòng.

# Một cặp số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng 1.

# Input

# Dòng đầu ghi số n (không quá 100).

# Dòng thứ 2 ghi n số của dãy A[]

# Output

# Ghi lần lượt các cặp số nguyên tố cùng nhau theo thứ tự tăng dần.

# Ví dụ


# Input

# Output

# 5


# 3 7 9 6 13


	
# 3 7

# 3 13

# 6 7

# 6 13

# 7 9

# 7 13

# 9 13

import sys

def GCD(a , b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    a = list(map(int, data[idx: idx + n])); idx += n

    a.sort()
    res = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            if GCD(a[i], a[j]) == 1:
                res.append(f"{a[i]} {a[j]}")

    print("\n".join(res))
if __name__ == "__main__":
    main()