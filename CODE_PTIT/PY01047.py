# Cho số nguyên dương N có không quá 500 chữ số.

# Hãy kiểm tra xem 4 chữ số cuối cùng ghép lại có tạo thành một số nguyên tố hay không.

# Chú ý: các chữ số 0 ở đầu trong 4 chữ số cuối vẫn được chấp nhận

# Input

# Dòng đầu ghi số bộ test (không quá 20).

# Mỗi test viết trên một dòng số nguyên dương N, không quá 500 chữ số.

# Output

# Với mỗi bộ test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 3


# 12234323130097


# 3443354654654654461123


# 43543543434554659999


	
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


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        n = int(s[-4:])
        print("YES" if is_prime(n) else "NO")

if __name__ =="__main__":
    main()