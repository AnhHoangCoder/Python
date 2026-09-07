# Cho dãy số A[] có N số nguyên dương. Người ta muốn biến đổi tất cả các số trong dãy về số nguyên tố. Tại mỗi bước, mỗi số chưa nguyên tố được phép tăng hoặc giảm 1 đơn vị để biến đổi dần về số nguyên tố gần nhất.

# Hãy tính xem cần ít nhất bao nhiêu bước cần thực hiện để biến đổi tất cả các phần tử của dãy về nguyên tố.

# Input

# Dòng đầu ghi số N là số phần tử của dãy (không quá 200).

# Dòng thứ 2 ghi N số của dãy, các giá trị đều nguyên dương và không quá 10000.

# Output

# Ghi ra số bước ít nhất tính được.

# Ví dụ


# Input

# Output

# 8


# 13 5 8 7 9 15 26 34


	
# 3
#Đề bài lỏ rõ là tổng số bước ít nhất nhưng thật ra là tìm số bước max
import sys

LIMIT = 20000

def solve_prime(limit):
    is_pr = [True] * (limit + 1)
    is_pr[0] = is_pr[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if is_pr[i]:
            for j in range(i * i, limit + 1, i):
                is_pr[j] = False
    return is_pr

def step_to_nearest_prime(x, is_pr):
    if x >= 2 and is_pr[x]:
        return 0
    d = 1
    while True:
        if x - d >= 2 and is_pr[x - d]:
            return d
        if x + d <= LIMIT and is_pr[x + d]:
            return d
        d += 1

def main():
    is_p = solve_prime(LIMIT)
    data = sys.stdin.read().split()
    idx = 0
    res = []
    while idx < len(data):
        n = int(data[idx]); idx += 1
        if n == 0:
            break
        a = list(map(int, data[idx : idx + n]))
        idx += n
        total = max(step_to_nearest_prime(x, is_p) for x in a)
        res.append(str(total))
    print("\n".join(res))

if __name__ == "__main__":
    main()