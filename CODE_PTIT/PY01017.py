# Cho một xâu ký tự có thể có các ký tự chữ cái và chữ số. Người ta thực hiện một phép mã hóa đơn giản, trong đó đếm từ trái qua phải các ký tự giống nhau liên tiếp và viết số đếm trước ký tự đó.

# Ví dụ: AACDDPQ được mã hóa thành 2A1C2D1P1Q

#            11111147g được mã hóa thành 6114171g

# Viết chương trình thực hiện thao tác mã hóa như trên.

# Input

# Dòng đầu ghi số bộ test. Mỗi dòng sau là một xâu ký tự, độ dài không quá 1000.

# Output

# Với mỗi bộ test, ghi ra xâu ký tự mã hóa tương ứng.

# Ví dụ


# Input

# Output

# 3


# AACDDPQ


# 11111147g


# 1111111111


	
# 2A1C2D1P1Q


# 6114171g


# 101

t = int(input())

for _ in range(t):
    s = input()
    result = []
    i = 0
    n = len(s)

    while i < n:
        count = 1
        while i + count < n and s[i + count] == s[i]:
            count += 1
        result.append(str(count) + s[i])
        i += count
    print("".join(result))