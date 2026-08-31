# Cho một số nguyên dương không quá 500 chữ số.

# Hãy kiểm tra xem số đó có thỏa mãn đồng thời ba tính chất sau hay không?

# Vị trí chẵn là chữ số chẵn
# Vị trí lẻ là chữ số lẻ
# Tổng chữ số là một số nguyên tố.
# Input

# Dòng đầu ghi số bộ test (không quá 10)

# Mỗi bộ test ghi trên một dòng giá trị số nguyên (không quá 500 chữ số)

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 2


# 2345678521


# 1212121212121212121212121


	
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
    sum = 0
    for i in range(0, len(s)):
        t = int(s[i])
        sum += t
        if i % 2 == 0:
            if t % 2 != 0:
                return False
        else:
            if t % 2 != 1:
                return False

    return is_prime(sum)


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    main()