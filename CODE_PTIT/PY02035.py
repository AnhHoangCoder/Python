# Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

# Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.

# Nhập thêm số nguyên dương K gọi là giá trị ngưỡng tối thiểu. Hãy liệt kê các số xuất hiện từ K lần trở lên trong dãy A[] theo thứ tự từ nhỏ đến lớn. 

# Input

# Dòng đầu ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

# Dòng thứ 2 ghi số nguyên dương K (không quá 100).

# Output

# Ghi ra lần lượt các số khác nhau của dãy A[] thỏa mãn xuất hiện ít nhất K lần và số lần xuất hiện tương ứng, mỗi số viết trên một dòng theo thứ tự tăng dần.

# Nếu không có số nào thỏa mãn ghi ra dòng chữ NOT FOUND

# Ví dụ


# Input

# Output

# 124356141111434356149


# 2


	
# 11 2


# 14 2


# 43 3


# 56 2




# 124356141111434356149


# 10


	
# NOT FOUND

def main():
    s = input()
    k = int(input())

    n = len(s)
    a = {}
    for i in range(0, n, 2):
        if i == n - 1:
            break

        num = int(s[i : i + 2])
        a[num] = a.get(num, 0) + 1

    flag = True
    res = []
    for key, value in sorted(a.items()):
        if value >= k:
            res.append(f"{key} {value}")
            flag = False
    print("NOT FOUND" if flag else "\n".join(res))

if __name__ == "__main__":
    main()