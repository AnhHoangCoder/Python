# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số. Xét các vị trí từ trái qua phải (tính từ 0). Hãy tính:

# Tích các chữ số ở vị trí chẵn – giá trị tích chữ số có thể đến 18 chữ số. Chú ý khi tính tích bỏ qua các chữ số 0.
# Tổng các chữ số ở vị trí lẻ
 

# Input

# Dòng đầu ghi số bộ test (không quá 20)
# Mỗi bộ test ghi trên một dòng số nguyên dương N (ít nhất 2 chữ số và không quá 500 chữ số)
# Output

# Với mỗi bộ test, viết trên một dòng hai giá trị: tích chữ số và tổng chữ số tính được.

# Ví dụ


# Input

# Output

# 3


# 12345678


# 20000


# 22334455667788


	
# 105 20


# 2 0


# 40320 35

def Sum(s):
    res = 0
    for i in range(1, len(s), 2):
        res += int(s[i])
    return res

def Mul(s):
    res = 1
    for i in range(0, len(s), 2):
        t = int(s[i])
        if t != 0:
            res *= t
    return res

def main():
    for _ in range(int(input())):
        s = input()
        print(f"{Mul(s)} {Sum(s)}")

if __name__ == "__main__":
    main()