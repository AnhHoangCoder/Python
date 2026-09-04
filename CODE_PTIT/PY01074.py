# Cho N số nguyên. Nhiệm vụ của bạn là phân tích các số nguyên đã cho dưới dạng tích của các thừa số nguyên tố, sau đó tính tổng các ước số nguyên tố này.

# Input:

# Dòng đầu tiên số nguyên N (1 ≤≤ N ≤ 106).

# N dòng tiếp theo, mỗi dòng gồm một số nguyên có giá trị không vượt quá 2*106.

# Output

# In ra một số nguyên là đáp án tìm được.

# Ví dụ


# Input:

# Output:

# 5 


# 7


# 9 


# 10 


# 13 


# 100


	
# 47



 

# Giải thích test:

# 7 = 7

# 9 = 3 x 3 à 3 + 3 = 6

# 10 = 2 x 5 à 2 + 5 = 7

# 13 = 13

# 100 = 2 x 2 x 5 x 5 à 2+2+5+5 = 14

# Cộng lại, 7 + 6 + 7 + 13 + 14 = 47.

import sys

input = sys.stdin.readline

N = int(input())
a = [int(input()) for _ in range(N)]

MAX = 2_000_000

# spf[i] = ước nguyên tố nhỏ nhất của i
spf = list(range(MAX + 1))

for i in range(2, int(MAX ** 0.5) + 1):
    if spf[i] == i:  # i là số nguyên tố
        for j in range(i * i, MAX + 1, i):
            if spf[j] == j:
                spf[j] = i

ans = 0

for x in a:
    while x > 1:
        ans += spf[x]
        x //= spf[x]

print(ans)