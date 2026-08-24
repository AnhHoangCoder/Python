# Cho số nguyên dương N không quá 6 chữ số.

# Hãy liệt kê các số nhỏ hơn N thỏa mãn cả ba điều kiện:

# N là số thuận nghịch
# Tất cả các chữ số của N đều chẵn
# Số chữ số của N cũng là một số chẵn
# Input

# Dòng đầu ghi số bộ test (không quá 10). Mỗi test viết một số N (22 < N <106)

# Output

# Ghi kết quả của mỗi test trên một dòng, mỗi số cách nhau đúng một khoảng trống.

# Ví dụ


# Input

# Output

# 2


# 30


# 100


	
# 22


# 22 44 66 88

import sys

def main():
    non_zero_even = [2, 4, 6, 8]
    even_digits = [0, 2, 4, 6, 8]

    result = []

    for d1 in non_zero_even:
        result.append(int(f"{d1}{d1}"))

    for d1 in non_zero_even:
        for d2 in even_digits:
            result.append(int(f"{d1}{d2}{d2}{d1}"))

    for d1 in non_zero_even:
        for d2 in even_digits:
            for d3 in even_digits:
                result.append(int(f"{d1}{d2}{d3}{d3}{d2}{d1}"))

    result.sort()
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []

    for i in range(1, t + 1):
        n = int(data[i])
        ans = [str(x) for x in result if x < n]
        out.append(" ".join(ans))

    print("\n".join(out)) 

if __name__ == "__main__":
    main()