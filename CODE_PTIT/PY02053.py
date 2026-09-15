# Cho ma trận vuông cấp N*N chỉ bao gồm các số nguyên dương.

# Với đường chéo phụ, ta sẽ chia ma trận thành 2 nửa, được gọi là nửa trên và nửa dưới của đường chéo phụ (không tính các phần tử nằm trên đường chéo phụ).



 

# Độ chênh lệch của ma trận được tính bằng trị tuyệt đối khi lấy tổng giá trị các phần tử ở nửa trên trừ đi tổng giá trị các phần tử ở nửa dưới.

# Nhập thêm một giá trị K gọi là ngưỡng cân đối của ma trận.  Trong trường hợp độ chênh lệch không quá K thì ma trận được coi là cân đối, nếu lớn hơn K thì không cân đối.

# Hãy xác định độ chênh lệch và tính cân đối của ma trận.

# Input

# Dòng đầu ghi số N (2 < N < 50)

# N dòng tiếp theo ghi các giá trị của ma trận, các số đều nguyên dương và không quá 1000.

# Dòng cuối ghi số K (0 < K <100)

# Output

# Dòng đầu ghi chữ YES hoặc NO

# Dòng thứ 2 ghi ra giá trị độ chênh lệch của ma trận

# Ví dụ


# Input

# Output

# 5


# 2 8 10 6 7


# 6 3 2 6 9


# 10 2 6 2 8


# 9 9 7 9 8


# 9 6 5 6 9


# 5


	
# NO


# 11

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    a = []

    for _ in range(n):
        a.append(list(map(int, data[idx : idx + n]))); idx += n

    k = int(data[idx]); idx += 1
    sum = 0

    for i in range(n):
        for j in range(n):
            if j < n - i - 1:
                sum += a[i][j]
            elif j > n - i - 1:
                sum -= a[i][j]

    ans = abs(sum)
    print("YES" if ans <= k else "NO")
    print(ans)

if __name__ == "__main__":
    main()