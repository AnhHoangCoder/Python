# Cho số nguyên dương N. Hãy kiểm tra xem N có thỏa mãn đồng thời hai tính chất sau đây hay không?

# Tổng chữ số của N chia hết cho 10
# Các chữ số cạnh nhau đều khác nhau đúng 2 đơn vị
# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test ghi trên một dòng số nguyên dương N. N có ít nhất 3 chữ số nhưng không quá 18 chữ số.

# Output

# Ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ


# Input

# Output

# 3


# 1353


# 246864


# 123435


	
# NO


# YES


# NO

t = int(input())

def check1(s : str) -> bool:
    sum = 0
    for c in s:
        sum += int(c)
    return sum % 10 == 0

def check2(s : str) -> bool:
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) != 2:
            return False
    return True

for _ in range(t):
    s = input()
    print("YES" if check1(s) and check2(s) else "NO")