# Một số nguyên dương được gọi là ưu thế nguyên tố nếu thỏa mãn cả hai điều kiện:

# Số chữ số của nó là một số nguyên tố
# Số lượng chữ số nguyên tố nhiều hơn số lượng chữ số không nguyên tố
# Viết chương trình kiểm tra một số nguyên có thỏa mãn ưu thế nguyên tố hay không.

# Input

# Dòng đầu ghi số bộ test, không quá 20.
# Mỗi bộ test ghi số nguyên dương N, ít nhất 3 chữ số nhưng không quá 500 chữ số
# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 3


# 1234567


# 22334455667


# 23400300489898989


	
# YES


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
    count = 0
    n = len(s)
    for i in range(n):
        if is_prime(int(s[i])):
            count += 1

    return count > n - count

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if is_prime(len(s)) and check(s) else "NO")

if __name__ == "__main__":
    main()