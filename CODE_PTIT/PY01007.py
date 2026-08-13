# Ngân hàng thông báo lãi suất là X % mỗi năm.

# Với số tiền gửi vào là N. Sau mỗi năm, tiền lãi sẽ được cộng dồn.

# Hỏi sau bao nhiêu năm thì số tiền đạt được ít nhất là M.

# Input

# Dòng đầu ghi số bộ test.

# Mỗi test viết 3 số thực (kiểu double) N, X và M. Trong đó 0<N<M<100000.

# Output

# Ghi ra số năm tính được.

# Ví dụ


# Input

# Output

# 2


# 200.00 6.5 300


# 500 4 1000.00


	
# 7


# 18

t = int(input())
for _ in range(t):
    n, x , m = map(float, input().split())
    year = 0

    while n < m:
        n *= (1 + x / 100)
        year += 1

    print(year)