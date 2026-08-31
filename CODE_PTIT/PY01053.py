# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

# Hãy kiểm tra xem N có chia hết cho 3 hay không.

# Input

# Dòng đầu ghi số bộ test (không quá 20).

# Mỗi test ghi số N (không quá 500 chữ số)

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 2


# 12341


# 123456789123456789


	
# NO


# YES

def check(s) -> bool:
    sum = 0
    for c in s:
        sum += int(c)

    return sum % 3 == 0

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    main()