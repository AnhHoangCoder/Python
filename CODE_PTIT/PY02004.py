# Cho dãy số A[] chỉ có các giá trị nhị phân 0 và 1.

# Hãy đếm xem có bao nhiêu cặp số khác nhau đứng cạnh nhau trong dãy.

# Input

# Dòng 1 ghi số N là số phần tử của dãy (không quá 100).

# Dòng 2 ghi N số nhị phân.

# Output

# Ghi ra kết quả bài toán.

# Ví dụ


# Input

# Output

# 6


# 1 0 0 1 1 1


	
# 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0

    for i in range(n - 1):
        if a[i] != a[i + 1]:
            count += 1

    print(count)

if __name__ == "__main__":
    main()