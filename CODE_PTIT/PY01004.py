# Trong toán học, một cặp số được gọi là nguyên tố cùng nhau nếu ước số chung lớn nhất của 2 số đó là 1. Cho số nguyên dương N, giả sử ta đếm được K số nguyên dương nhỏ hơn N có tính chất nguyên tố cùng nhau với N. Hãy kiểm tra xem K có phải là số nguyên tố hay không.

# Input

# Dòng đầu ghi số bộ test, không quá 10.

# Dòng thứ 2 ghi số N (1 < N < 10000)

# Output

# Với mỗi test ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 2


# 2


# 3


	
# NO


# YES

t = int(input())

def prime(n : int) -> bool:
    if n < 2:
        return False
    for i in range(2, (int)(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a , b):
    while b != 0:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    count = 0
    for k in range(1, n, 1):
        if gcd(k, n) == 1:
            count += 1

    print("YES" if prime(count) else "NO")
