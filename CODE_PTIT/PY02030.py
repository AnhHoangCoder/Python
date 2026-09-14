# Cho dãy số A[] có N phần tử là các số nguyên dương không quá 1000. Sau khi loại bỏ tất cả các giá trị bị lặp lại ở trong A[] ta tạo được dãy B[] có m phần tử là các giá trị khác nhau theo đúng thứ tự xuất hiện trong dãy A[].

# Hãy tìm vị trí i nhỏ nhất (tính từ 0) trong dãy B[] thỏa mãn:

# Tổng các phần tử từ B[0] đến B[i] là một số nguyên tố
# Tổng các phần tử từ B[i+1] đến B[m-1] cũng là một số nguyên tố.
# Input

# Dòng đầu ghi số N (1 < N < 500).

# Dòng tiếp theo ghi N số của dãy A[]

# Output

# Ghi ra vị trí i đầu tiên tìm được.

# Nếu không có vị trí thỏa mãn thì ghi ra dòng chữ NOT FOUND

# Ví dụ


# Input

# Output

# 10


# 3 6 7 3 4 7 3 6 4 4


	
# 0




# 10


# 3 6 7 3 5 7 3 6 6 7


	
# NOT FOUND



# Giải thích test 1:

# Dãy B[] = {3, 6, 7, 4}

# Vị trí 0 thỏa mãn vì 3 là số nguyên tố; 6+7+4 = 17 cũng là số nguyên tố.

import sys

def is_prime(n : int) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1

    a = list(map(int, data[idx : idx + n]))
    b = []
    seen = set()
    for x in a:
        if not x in seen:
            seen.add(x)
            b.append(x)

    m = len(b)
    prefix = [0] * (m + 1)
    prefix[0] = b[0]

    for i in range(1, m):
        prefix[i] = prefix[i - 1] + b[i]

    flag = False
    ans = -1
    for i in range(0, m):
        if is_prime(prefix[i]) and is_prime(prefix[m - 1] - prefix[i]):
            flag = True
            ans = i
            break

    print(f"{ans}" if flag else "NOT FOUND")

if __name__ == '__main__':
    main()
