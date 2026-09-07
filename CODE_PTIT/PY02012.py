# Cho dãy số A[] có n phần tử. Hãy sắp xếp các số chẵn trong dãy theo thứ tự tăng dần và các số lẻ theo thứ tự giảm dần.

# In ra dãy kết quả đã sắp xếp trong đó vị trí số chẵn và vị trí số lẻ không thay đổi so với dãy ban đầu.

# Input

# Dòng đầu ghi số n (1 < n ≤ 1000)

# Các dòng tiếp theo ghi đủ n số của dãy A[], các số đều nguyên dương và không quá 1000.

# Output

# Ghi ra dãy kết quả đã sắp xếp trong đó các vị trí của số chẵn và số lẻ không thay đổi.

# Ví dụ


# Input

# Ouput

# 10


# 1 2 3 4 5 6 7 7 9 6


	
# 9 2 7 4 7 6 5 3 1 6

import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:n + 1]))

    idx_chan, val_chan = [], []
    idx_le, val_le = [], []

    for i in range(n):
        if a[i] % 2 == 0:
            idx_chan.append(i)
            val_chan.append(a[i])
        else:
            idx_le.append(i)
            val_le.append(a[i])

    val_chan.sort()
    val_le.sort(reverse=True)

    res = [0] * n
    for pos, val in zip(idx_chan, val_chan):
        res[pos] = val
    for pos, val in zip(idx_le, val_le):
        res[pos] = val
    
    print(*res)


if __name__ == "__main__":
    main()