# Nhập số nguyên dương N (1 < N < 10000).

# Viết chương trình tính tổng:

# S = 1 + 1/3 + 1/5 + … + 1/N nếu N lẻ
# S = 1/2 + 1/4 + 1/6 + … + 1/N nếu N chẵn
# Kết quả được in ra với 6 chữ số phần thập phân.

# Input

# Dòng đầu ghi số bộ test, không quá 10.

# Mỗi test ghi một số N

# Output

# Với mỗi bộ test, ghi ra kết quả trên một dòng.

# Ví dụ


# Input

# Output

# 2


# 10


# 15


	
# 1.141667


# 2.021800

t = int(input())

def Sum(n : int):
    S = 0.0
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            S += (1 / i)
    else:
        for i in range(1, n + 1, 2):
            S += (1 / i)
    return S
for _ in range(t):
    n = int(input())
    print(f"{Sum(n):.6f}")