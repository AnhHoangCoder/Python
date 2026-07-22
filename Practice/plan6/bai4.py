#Đệ quy + ghi nhớ: đếm số cách leo cầu thang

def count_stairs(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = count_stairs(n-1, memo) + count_stairs(n-2, memo)
    return memo[n]

t = int(input("Nhap so test case: "))
for _ in range(t):
    n = int(input("Nhap so n: "))
    print(count_stairs(n, None))