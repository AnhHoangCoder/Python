# Khai báo lớp Phân số gồm hai thuộc tính tử số và mẫu số. Các giá trị đều nguyên dương và không quá 18 chữ số.

# Nhập vào một phân số và in ra phân số đó ở dạng tối giản.

# Input

# Có hai số nguyên dương lần lượt là tử số và mẫu số.

# Output

# Ghi ra phân số tối giản như trong ví dụ

# Ví dụ

# Input

# Output

# 123 456

	
# 41/152

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

class fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def simplified_fraction(self):
        gcd = GCD(self.a, self.b)
        print(f"{self.a // gcd}/{self.b // gcd}")

def main():
    a, b = map(int, input().split())
    ans = fraction(a, b)
    ans.simplified_fraction()

if __name__ == '__main__':
    main()