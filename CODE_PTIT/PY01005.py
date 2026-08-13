# Chữ số 4 và chữ số 7 được xem là các chữ số may mắn.

# Cho số nguyên dương N có không quá 18 chữ số. Hãy đếm xem số chữ số 4 cộng với số chữ số 7 trong N có phải bằng 4 hay bằng 7 hay không.

# Input

# Chỉ có số N

# Output

# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ

# Input

# Output

# 40047

	
# NO


# 7747774

	
# YES


# 1000000000000000000

	
# NO

n = int(input())
ch4 ,ch7 = 0, 0

while n > 0:
    a = n % 10
    if a == 4:
        ch4 += 1
    elif a == 7:
        ch7 += 1
    n //= 10

res = ch4 + ch7
print("YES" if res == 4 or res == 7 else "NO")