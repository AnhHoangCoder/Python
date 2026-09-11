# Cho dãy số a[] có n phần tử và dãy số b[] có m phần tử là các số nguyên dương nhỏ hơn 1000. Gọi tập hợp A là tập các số khác nhau trong a[], tập hợp B là tập các số khác nhau trong b[].

# Hãy tìm tập giao của A và B, hiệu A – B và hiệu B – A. Mỗi tập kết quả viết trên một dòng theo thứ tự từ nhỏ đến lớn.

# Input

# Dòng đầu ghi 2 số n và m (1 < n,m <100).

# Dòng thứ 2 ghi n số của a[].

# Dòng thứ 3 ghi m số của b[].

# Các số đều dương và nhỏ hơn 1000.  

# Output

# Dòng đầu ghi tập giao của A và B

# Dòng thứ 2 ghi tập A – B

# Dòng thứ 3 ghi tập B - A

# Ví dụ


# Input

# Output

# 5 6


# 1 2 3 4 5


# 3 4 5 6 7 8


	
# 3 4 5


# 1 2


# 6 7 8

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0

    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    a = set(map(int, data[idx: idx + n])); idx += n
    b = set(map(int, data[idx: idx + m])); idx += m

    print(*sorted(a & b))
    print(*sorted(a - b))
    print(*sorted(b - a))

if __name__ == "__main__":
    main()