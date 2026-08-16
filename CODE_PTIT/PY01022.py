# Cho một số nguyên (có thể âm) không quá 100.000 chữ số. Mỗi bước thực hiện thay thế số nguyên này bằng giá trị tổng chữ số của số đó. Hỏi sau mấy bước thì số đó chỉ còn duy nhất 1 chữ số.

# Input

# Chỉ có duy nhất số nguyên N (không quá 100.000 chữ số)

# Output

# Ghi ra số bước cần thực hiện.

# Ví dụ

# Input

# Output

# 10

	
# 1


# 919

	
# 3


# 6

	
# 1

n = input().strip().lstrip('-')

cnt = 0
while len(n) > 1:
    n = str(sum(map(int, n)))
    cnt += 1
print(cnt)