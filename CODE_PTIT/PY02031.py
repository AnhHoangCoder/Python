# Cho ma trận A[] cỡ N*M chỉ bao gồm các số nguyên dương không quá 1000. Hãy kiểm tra các số trong ma trận, nếu giá trị nào là số nguyên tố thì thay thế bằng số 1, không phải thì thay thế bằng số 0.

# Input

# Dòng đầu ghi 2 số N và M là kích thước ma trận (1 < N,M < 20)

# N dòng tiếp theo mỗi dòng có M số mô tả ma trận

# Output

# Ghi ra ma trận kết quả

# Ví dụ


# Input

# Output

# 3 3


# 1 2 3


# 4 5 6


# 7 8 9


	
# 0 1 1


# 0 1 0


# 1 0 0

import sys

def solve(n):
    pr = [True] * (n + 1)
    pr[0] = pr[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if pr[i]:
            for j in range(i * i, n + 1, i):
                pr[j] = False
    return pr

def main():
    primes = solve(1000)
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    a = []

    for i in range(n):
        a.append(list(map(int, data[idx: idx + m])))
        idx += m

    res = []
    for i in range(n):
        s = ""
        for j in range(m):
            if primes[a[i][j]]:
                s += "1"
            else:
                s += "0"

            if j < m - 1:
                s += " "
        res.append(s)
    print("\n".join(res))

if __name__ == "__main__":
    main()