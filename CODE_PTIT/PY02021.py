# Cho dãy số A[], B[] và C[] là dãy không giảm và có lần lượt N, M, K phần tử. Nhiệm vụ của bạn là hãy tìm các phần tử chung của 3 dãy số này.

# Input:

# Dòng đầu tiên là số lượng bộ test T (T ≤ 20).

# Mỗi test gồm số nguyên N, M và K (1≤ N, M, K ≤ 100 000).

# Dòng tiếp theo gồm N số nguyên A[i], rồi M số nguyên B[i] và K số nguyên C[i].

# (0 ≤ A[i], B[i], C[i] ≤ 109).

# Output: 

# Với mỗi test, in ra trên một dòng là đáp án thu được. Nếu không tìm được đáp án, in ra “NO”.

 

# Ví dụ:


# Input:

# Output

# 3


# 6 5 8


# 1 5 10 20 40 80


# 5 7 20 80 100


# 3 4 15 20 30 70 80 120


# 3 5 4


# 1 5 5


# 3 4 5 5 10


# 5 5 10 20


# 3 3 3


# 1 2 3


# 4 5 6


# 7 8 9


	
# 20 80


# 5 5


# NO

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx]); idx += 1
    ans = []
    for _ in range(t):
        n, m, k = map(int, data[idx: idx + 3]); idx += 3

        a = list(map(int, data[idx: idx + n])); idx += n
        b = list(map(int, data[idx: idx + m])); idx += m
        c = list(map(int, data[idx: idx + k])); idx += k

        res = []
        i = j = l = 0

        while i < n and j < m and l < k:
            if a[i] == b[j] == c[l]:
                res.append(a[i])
                i += 1
                j += 1
                l += 1

            elif a[i] < b[j]:
                i += 1
            elif b[j] < c[l]:
                j += 1
            else:
                l += 1

        if not res:
            ans.append("NO")
        else:
            ans.append(" ".join(map(str, res)))
    
    print("\n".join(ans))

    
if __name__ == "__main__":
    main()