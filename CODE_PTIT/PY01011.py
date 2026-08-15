# Cho số nguyên dương N, hãy liệt kê các số thuận nghịch M nhỏ hơn N và thỏa mãn điều kiện:

# Chỉ có các chữ số 0,2,4,6,8
# Số M có số lượng các chữ số là chẵn
# Input

# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

# Output

# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

# Ví dụ


# Input

# Output

# 2


# 30


# 100


	
# 22


# 22 44 66 88

t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    for i in range(22, n, 2):
        s = str(i)

        if len(s) % 2 != 0:
            continue

        if any(c not in "02468" for c in s):
            continue

        if s == s[::-1]:
            ans.append(s)

    print(" ".join(ans))

    