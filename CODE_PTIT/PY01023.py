# Cho số nguyên dương N. Hãy phân tích N thành tích các thừa số nguyên tố. Kết quả được in ra theo mẫu trong ví dụ, trong đó thêm số thừa số 1 (không phải nguyên tố) ở đầu kết quả phân tích.

# Input

# Dòng đầu ghi số bộ test, mỗi test ghi trên một dòng số nguyên dương N không quá 6 chữ số.

# Output

# Ghi ra kết quả phân tích theo mẫu như trong ví dụ.

# Ví dụ


# Input

# Output

# 3


# 28


# 100


# 1234


	
# 1 * 2^2 * 7^1


# 1 * 2^2 * 5^2


# 1 * 2^1 * 617^1

t = int(input())

for _ in range(t):
    n = int(input())
    print(1,end = '')
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            print(f" * {i}^{cnt}", end = "")     
    if n > 1:
        print(f" * {n}^1")
    else:
        print()
    
    