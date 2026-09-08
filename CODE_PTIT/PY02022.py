# Cho dãy số nguyên dương A[] có N phần tử. Hãy viết chương trình liệt kê các số nguyên tố khác nhau và số lần xuất hiện của số đó trong dãy ban đầu.

# Các số được liệt kê theo thứ tự xuất hiện.

# Input

# Dòng đầu ghi số N (không quá 500).

# Dòng sau ghi N số của dãy (không quá 6 chữ số).

# Output

# Ghi ra các số nguyên tố khác nhau trong dãy theo thứ tự xuất hiện và số lần xuất hiện. Mỗi số liệt kê trên 1 dòng.

# Ví dụ


# Input

# Output

# 10


# 2 4 7 5 7 8 9 3 7 2


	
# 2 2


# 7 3


# 5 1


# 3 1

import sys

def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    a = list(map(int, data[idx: idx + n])); idx += n

    ans = {}
    res = []
    for x in a:
        ans[x] = ans.get(x, 0) + 1

    for key, value in ans.items():
        if isPrime(key):
            res.append(f"{key} {value}")

    print("\n".join(res))

if __name__ == "__main__":
    main()