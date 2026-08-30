# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

# Hãy kiểm tra xem tổng các chữ số của N có phải là một số nguyên tố hay không.

# Input

# Dòng đầu ghi số bộ test (không quá 20).

# Mỗi test ghi số N (không quá 500 chữ số)

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 2


# 12341


# 22222222222222222222


	
# YES


# NO

import math

def is_prime(n) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def check(s) -> bool:
    total = 0
    for c in s:
        total += int(c)

    return is_prime(total)

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    main()
