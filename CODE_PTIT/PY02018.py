# Cho dãy số A[] có N phần tử là các số nguyên dương khác nhau. Hãy tìm số nhỏ nhất còn thiếu trong dãy số đó.

# Input

# Dòng đầu ghi số N (1 <= N <= 30000).

# Dòng tiếp theo ghi N số của dãy A (1 <= A[i] <= 30000).

# Output

# Ghi ra số nhỏ nhất còn thiếu nếu có.

# (khi dãy số đầy đủ các số từ 1 đến N thì số nhỏ nhất còn thiếu sẽ là N+1).

# Ví dụ


# Input

# Output

# 3


# 1 2 4


	
# 3

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    a = list(map(int, data[idx: idx + n])); idx += n

    seen = [False] * (n + 2)
    for x in a:
        if 1 <= x <= n + 1:
            seen[x] = True

    ans = n + 1
    for i in range(1, n + 1):
        if not seen[i]:
            ans = i
            break

    print(ans)


if __name__ == "__main__":
    main()