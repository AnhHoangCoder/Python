# Nhập xâu s1, giả sử gọi xâu đảo là s2. Hãy kiểm tra xem khoảng cách ký tự cạnh nhau trong hai xâu có thỏa mãn công thức sau hay không:

# |s1[i] – s1[i-1]| = |s2[i] – s2[i-1]| với tất cả giá trị 0 < i < N

 

# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test là một xâu ký tự độ dài không quá 100000. Không có khoảng trống.

# Output

# Ghi ra YES hoặc NO.

# Ví dụ


# Input

# Output

# 2


# acxz


# bcxz


	
# YES


# NO

def solve(s1 : str, s2 : str) -> bool:
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return False
    return True

t = int(input())

for _ in range(t):
    s1 = input()
    s2 = s1[::-1]

    print("YES" if solve(s1, s2) else "NO")