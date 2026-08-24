# Một số nguyên dương được gọi là số tăng giảm nếu thỏa mãn các điều kiện:

# Có từ 3 chữ số trở lên
# Tìm ra một vị trí trong dãy chữ số sao cho từ bên trái đến vị trí đó thỏa mãn thứ tự tăng dần (tăng chặt) còn từ vị trí đó đến hết thì thỏa mãn thứ tự giảm dần (giảm chặt).
# Viết chương trình kiểm tra một số có phải số tăng giảm hay không.

# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test viết trên một dòng số nguyên dương N không quá 18 chữ số

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Ouput

# 3


# 12342


# 23342


# 5678961


	
# YES


# NO


# YES

def check(s) -> bool:
    n = len(s)
    i = 0
    while i < n - 1 and s[i] < s[i + 1]:
        i += 1

    if i == 0:
        return False
    
    while i < n - 1 and s[i] > s[i + 1]:
        i += 1
    
    return i > 0 and i == n - 1

t = int(input())
for _ in range(t):
    s = input()
    print("YES" if check(s) else "NO")