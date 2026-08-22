# Cho một số nguyên dương N. Mỗi bước bạn thực hiện tính tổng của N với giá trị số đảo ngược của N. Bạn sẽ dừng lại khi gặp giá trị chia hết cho 7 hoặc khi đã thực hiện quá 1000 bước lặp.

# Hãy tính giá trị chia hết cho 7 tìm được theo thủ tục trên hoặc ghi ra -1 nếu không thể tìm ra đáp án.

# Input:

# Dòng đầu ghi số bộ test (không quá 1000).

# Mỗi test ghi số N (1 ≤ N ≤ 1018)

# Output:

# Ghi ra giá trị chia hết cho 7 đầu tiên tìm được. Hoặc số -1 nếu không thể tìm được đáp án.

# Ví dụ:


# Input

# Output

# 5


# 1


# 2


# 3


# 4


# 999999


	
# 77


# 77


# 9447438


# 77


# 999999



# Giải thích test 1: 1 -> 2 -> 4 -> 8 -> 16 -> 77

def numReverse(s):
    ans = 0
    for i in range(len(s) - 1, -1, -1):
        ans = ans * 10 + (ord(s[i]) - ord('0'))
    return ans

t = int(input())
for _ in range(t):
    s = input()
    if int(s) % 7 == 0:
        print(s)
        continue
    tmp = s
    count = 0
    check = False
    while count < 1000:

        n1 = int(tmp)
        n2 = numReverse(tmp)

        sum = n1 + n2
        if sum % 7 == 0:
            print(sum)
            check = True
            break
        count += 1
        tmp = str(sum)

    if count == 1000 and not check:
        print(-1)
