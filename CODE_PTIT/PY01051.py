# Cho số nguyên dương N có thể rất lớn nhưng không quá 500 chữ số.

# Hãy kiểm tra xem tổng các chữ số của N có phải là một số thuận nghịch hay không.

# Một số chỉ được coi là thuận nghịch nếu nhiều hơn 1 chữ số và số đảo của nó đúng bằng nó.

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


# 22222222222222222222


	
# YES


# NO

def check_sum(s) -> bool:
    total = 0
    for c in s:
        total += int(c)

    ans = str(total)
    return len(ans) > 1 and ans == ans[::-1]

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if check_sum(s) else "NO")

if __name__ == "__main__":
    main()