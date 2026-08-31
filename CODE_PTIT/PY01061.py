# Cho số nguyên dương N có ít nhất 4 chữ số và không quá 500 chữ số.

# Một số được gọi là số đầu cuối nguyên tố nếu thỏa mãn cả hai điều kiện:

# Ba chữ số đầu ghép lại được một số nguyên tố
# Ba chữ số cuối ghép lại được một số nguyên tố
# Viết chương trình kiểm tra xem N có phải là đầu cuối nguyên tố hay không?

# Input

# Dòng đầu ghi số bộ test (không quá 20).

# Mỗi bộ test viết trên một dòng số N, ít nhất 4 chữ số và không quá 500 chữ số.

# Output

# Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 3


# 12743


# 7337


# 12345678901234


	
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
    if len(s) < 4:
        return False

    num1 = int(s[:3])
    num2 = int(s[-3:])

    return is_prime(num1) and is_prime(num2)

def main():
    for _ in range(int(input())):
        s = input()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    main()