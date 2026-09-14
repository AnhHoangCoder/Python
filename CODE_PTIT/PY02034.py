# Cho một dãy ký tự số không quá 1000 chữ số và không có chữ số 0.

# Người ta lần lượt lấy ra mỗi lần 2 chữ số tính từ trái sang phải. Nếu bước cuối cùng không đủ hai chữ số thì bỏ qua chữ số đó. Kết quả sẽ được một dãy số nguyên dương A[] chỉ bao gồm các số có hai chữ số.

# Hãy liệt kê và đếm các số khác nhau xuất hiện trong A[] theo thứ tự xuất hiện.

# Input

# Chỉ có một dòng ghi dãy ký tự số (độ dài không quá 1000). Dữ liệu vào đảm bảo không có chữ số 0.

# Output

# Ghi ra lần lượt các số khác nhau xuất hiện trong dãy A[] và số lần xuất hiện tương ứng, mỗi số viết trên một dòng.

# Ví dụ



# Input

# Output

# 124356141111434356149

	
# 12 1


# 43 3


# 56 2


# 14 2


# 11 2

def main():
    s = input()

    count = {}
    n = len(s)

    for i in range(0, n, 2):
        if i == n - 1:
            break
        num = int(s[i : i + 2])
        count[num] = count.get(num, 0) + 1

    res = []
    for key, value in count.items():
        res.append(f"{key} {value}")
    print("\n".join(res))

if __name__ == "__main__":
    main()