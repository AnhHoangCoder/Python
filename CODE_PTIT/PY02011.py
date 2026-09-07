# Cho dãy số A[] có N phần tử là các số nguyên dương.

# Mỗi bước bạn được phép thay đổi 1 giá trị trong dãy bằng cách tăng lên 1 hoặc giảm đi 1.

# Hãy tính xem cần ít nhất bao nhiêu bước để biến đổi dãy về giá trị bằng nhau, với điều kiện giá trị của dãy bằng nhau đó phải là một trong các giá trị ban đầu của dãy.

# Input

# Dòng đầu ghi số N là số phần tử của dãy (không quá 200).

# Dòng thứ 2 ghi N phần tử của dãy, các phần tử đều nguyên dương và không quá 10000.

# Output

# Ghi ra tổng số bước ít nhất tìm được và giá trị bằng nhau được chọn.

# Trong trường hợp có nhiều giá trị có thể chọn thì chọn số đầu tiên theo thứ tự xuất hiện trong dãy ban đầu.

# Ví dụ


# Input

# Output

# 8


# 13 5 8 7 9 15 26 34


	
# 59 13

import bisect

# def solve_n2(a):
#     best_cost, best_value = float('inf'), None
#     for v in a:
#         cost = sum(abs(x - v) for x in a)
#         if cost < best_cost:
#             best_cost, best_value = cost, v
#     return best_cost, best_value


def solve_nLogn(a, n):
    sorted_a = sorted(a)

    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + sorted_a[i]
    total_sum = prefix[n]

    def cost(v):
        pos = bisect.bisect_right(sorted_a, v)
        left_sum = prefix[pos]
        right_sum = total_sum - left_sum
        left_count = pos
        right_count = n - pos
        return (v * (left_count) - left_sum) + (right_sum - v * (right_count))

    best_cost, best_value = float('inf'), None
    for v in a:
        c = cost(v)
        if c < best_cost:
            best_cost = c
            best_value = v
    return best_cost, best_value
     
def main():
    n = int(input())
    a = list(map(int, input().split()))

    solve_nLogn(a, n)
    cost, value = solve_nLogn(a , n)
    print(cost , value)

if __name__ == "__main__":
    main()