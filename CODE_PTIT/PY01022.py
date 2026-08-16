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

#Bài này đáng nhẽ ra len(n) == 1 thì cnt = 0 nhưng đề bài bảo éo

n = input()

def step(s):
    if len(s) == 1:
        return 0

    sum = 0
    for i in s: sum += ord(i) - ord('0')
    return 1 + step(str(sum))

print(1 if len(n) <= 1 else step(n))