# Một số nguyên dương được gọi là đẹp nếu số đó chỉ có hai chữ số khác nhau và các chữ số ở cách nhau 2 vị trí đều bằng nhau. Ví dụ: 121, 1313131, 5656 …

# Viết chương trình kiểm tra một số có phải số đẹp hay không?

# Input

# Dòng đầu ghi số bộ test. Mỗi bộ test ghi một số nguyên dương N (lớn hơn 10 và có không quá 18 chữ số) trên một dòng.

# Output

# Với mỗi bộ test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra.

# Ví dụ


# Input

# Output

# 3


# 12121212


# 343433


# 78789989


	
# YES


# NO


# NO

import sys

def is_dep(s):
    nums = set(s)

    if len(nums) != 2:
        return False

    for i in range(len(s) - 2):
        if s[i] != s[i + 2]:
            return False

    return True

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        n = data[i]
        results.append("YES" if is_dep(n) else "NO")
    print("\n".join(results))

if __name__ == "__main__":
    main()