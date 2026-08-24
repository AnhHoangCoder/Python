# Hệ cơ số 3 chỉ biểu diễn các số sử dụng ba chữ số là 0, 1, 2.

# Nhập vào dãy biểu diễn không quá 18 ký tự, hãy kiểm tra xem dãy biểu diễn nào là đúng với hệ cơ số 3.

# Input

# Dòng đầu là số bộ test, mỗi dòng tiếp theo ghi một dãy biểu diễn cần kiểm tra.

# Output

# Nếu đúng in ra YES, nếu sai in ra NO.

# Ví dụ

# Input

# Output

# 3

# 1214AB

# 10210221

# 22222222
	
# NO


# YES


# YES

import sys

def checkCoSo3(s) -> bool:
    for c in s:
        if c not in "012":
            return False
    return True

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = data[i]
        results.append("YES" if checkCoSo3(n) else "NO")

    print("\n".join(results))

if __name__ == "__main__":
    main()
