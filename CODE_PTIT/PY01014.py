# Cho ba số nguyên dương a, K, N. Hãy liệt kê tất cả các số nguyên dương b thỏa mãn cả hai điều kiện:

# a + b ≤ N
# a + b chia hết cho K
# Input

# Chỉ có một dòng ghi ba số nguyên dương theo thứ tự a, K, N (không quá 9 chữ số).

# Output

# Ghi ra lần lượt các số b tìm được theo thứ tự tăng dần.

# Nếu không tìm được số nào in ra -1

# Ví dụ

# Input

# Output

# 10 1 10

	
# -1


# 10 6 40

	
# 2 8 14 20 26

def solve(a, K, N):
    r = a % K
    b0 = K - r

    if a + b0 > N:
        return "-1"

    result = []
    b = b0

    while a + b <= N:
        result.append(str(b))
        b += K

    return " ".join(result)

a, K, N = map(int, input().split())
print(solve(a, K, N))