# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

# Hãy tính tích các chữ số của N. Chú ý bỏ qua các chữ số 0 nếu có. 

# Input

# Dòng đầu ghi số bộ test (không quá 20).

# Mỗi test ghi số N (không quá 500 chữ số).

# Output

# Với mỗi bộ test, ghi ra kết quả tính được.

# Dữ liệu vào đảm bảo kết quả tích các chữ số sẽ không vượt quá 18 chữ số.  

# Ví dụ


# Input

# Output

# 2


# 123410


# 123456789123456789


	
# 24


# 131681894400

def mul(s):
    res = 1
    for c in s:
        t = int(c)
        if t != 0:
            res *= t
    return res
    
def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(mul(s))

if __name__ == "__main__":
    main()