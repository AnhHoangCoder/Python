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

def is_prime(n : int) -> bool:
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
    if not is_prime(len(s)):
        return False
    count = 0
    for c in s:
        t = int(c)
        if is_prime(t):
            count += 1

    return count > len(s) - count

def main():
    for _ in range(int(input())):
        s = input()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    main()