# Cho dãy số A[] có N phần tử đều là các số nguyên dương, không quá 6 chữ số.

# Hãy sắp xếp dãy số theo tổng chữ số tăng dần. Nếu tổng chữ số bằng nhau thì số nào nhỏ hơn sẽ viết trước.

# Input

# Dòng đầu ghi số bộ test (không quá 10)

# Mỗi bộ test gồm 2 dòng:

# Dòng đầu là số N (N < 100)
# Dòng thứ 2 ghi N số của mảng A[], các số đều nguyên dương và không quá 9 chữ số.
# Output

# Với mỗi bộ test, ghi trên một dòng dãy số kết quả.

# Ví dụ


# Input

# Output

# 1


# 8


# 143 43 22 99 7 9 1111 10000000


	
# 10000000 22 1111 7 43 143 9 99

import sys

def sum_number(n):
    return sum(int(d) for d in str(abs(n)))

def main():
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx]); idx += 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx: idx + n])); idx += n

        parts = [(x, sum_number(x)) for x in a]
        ans = sorted(parts, key = lambda x: (x[1], x[0]))
        print(*[x for x, _ in ans])

if __name__ == "__main__":
    main()