# Cho dãy số A[] gồm có N phần tử. Nhiệm vụ của bạn là hãy tìm một số có tần số xuất hiện nhiều nhất, yêu cầu lớn hơn N/2 lần xuất hiện trong dãy số.

# Input:

# Dòng đầu tiên là số lượng bộ test T (T ≤ 10).

# Mỗi test gồm số nguyên N (1≤ N ≤ 100 000), số lượng phần tử trong dãy số ban đầu.

# Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 1 000 000).

# Output: 

# Với mỗi test in ra đáp án của bài toán trên một dòng. Nếu có nhiều số cùng có tần số xuất hiện nhiều nhất như nhau và đều thỏa mãn số lần lớn hơn N/2 thì in ra số nhỏ nhất.

# Nếu không tìm được đáp án, in ra “NO”.

# Ví dụ:


# Input:

# Output

# 2


# 9


# 3 3 4 2 4 4 2 4 4


# 8


# 3 3 4 2 4 4 2 4


	
# 4


# NO

import sys

def main():
    data = sys.stdin.read().split()
    idx = 0
    res = []
    t = int(data[idx]); idx += 1

    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx: idx + n]))
        idx += n

        count = {}
        for x in a:
            count[x] = count.get(x, 0) + 1

        best_key, best_value = float('inf'), float('-inf')
        flag = False

        for key, value in count.items():
            if value > n / 2:
                flag = True
                if value > best_value or (value == best_value and key < best_key):
                    best_value = value
                    best_key = key

        res.append(str(best_key) if flag else "NO")

    print("\n".join(res))

if __name__ == "__main__":
    main()