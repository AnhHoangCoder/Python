# Dãy số Fibonacci được định nghĩa theo công thức như sau:

# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 với n>2
# Cho hai số nguyên dương a và b (1 < a < b < 93). Viết chương trình liệt kê các số Fibonacci từ a đến b.

# Input

# Dòng đầu ghi số bộ test, không quá 10.

# Mỗi bộ test viết trên một dòng hai số a và b.

# Output

# Ghi ra kết quả của mỗi test trên một dòng, mỗi số cách nhau một khoảng trống.

# Ví dụ


# Input

# Output

# 1


# 1 10


	
# 1 1 2 3 5 8 13 21 34 55

def main():
    fb = [0] * 93
    fb[1] = 1
    fb[2] = 1
    for i in range(3, 93):
        fb[i] = fb[i - 1] + fb[i - 2]

    for _ in range(int(input())):
        a, b = map(int, input().split())
        while a < b:
            print(fb[a], end = " ")
            a += 1
        print(fb[a])

if __name__ == "__main__":
    main()