# Cho dãy số nguyên dương A[] có N phần tử. Các giá trị trong dãy không quá 1000.

# Hãy sắp xếp các số nguyên tố trong dãy theo thứ tự tăng dần. Các giá trị không nguyên tố vẫn giữ nguyên vị trí như lúc đầu.

# Xem ví dụ để hiểu rõ hơn yêu cầu bài toán.

# Input

# Dòng đầu ghi số N (1 < N < 100), dòng thứ 2 ghi N số của dãy A[].

# Output

# Ghi ra dãy số kết quả trên một dòng.

# Ví dụ


# Input

# Output

# 8


# 4 6 3 8 7 2 5 9


	
# 4 6 2 8 3 5 7 9

import sys

def is_prime(n : int) -> bool:
    if n < 2:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1

    a = list(map(int, data[idx : idx + n]))
    idxPr = []; pr = []
    for i in range(n):
        if is_prime(a[i]):
            pr.append(a[i])
            idxPr.append(i)

    pr.sort()
    for key, value in zip(idxPr, pr):
        a[key] = value

    print(" ".join(map(str, a)))

if __name__ == "__main__":
    main()