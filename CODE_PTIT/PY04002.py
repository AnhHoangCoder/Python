# Khai báo lớp Rectangle với 3 thuộc tính:

# Chiều dài: số nguyên
# Chiều rộng: số nguyên
# Màu sắc: xâu ký tự
# Nhập vào giá trị độ dài hai cạnh của hình chữ nhật và màu sắc. In ra thông tin về chu vi, diện tích và màu sắc (đã đưa về dạng chuẩn trong đó ký tự đầu viết hoa, các ký tự sau viết thường) của hình chữ nhật đó.

# Input

# Gồm 2 số nguyên là độ dài 2 cạnh hình chữ nhật và một xâu ký tự (không có khoảng trống) mô tả màu sắc.

# Output

# Nếu hình chữ nhật là hợp lệ (các cạnh đều nguyên dương) thì in ra 3 thông tin: chu vi, diện tích, màu sắc, mỗi thông tin cách nhau một khoảng trống.

# Nếu dữ liệu không hợp lệ in ra INVALID

# Ví dụ

# Input

# Output

# 10 2 RED

	
# 24 20 Red


#Hàm main cố định

# if __name__ == '__main__':
#     arr = input().split()
#     r = Rectangle(int(arr[0]), int(arr[1]), int(arr[2]))
#     print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))


#main() đề bài cho cố định là sai, để giống input thì phải bỏ int đi
class Rectangle:
    def __init__(self, dai, rong, color):
        self.dai = dai
        self.rong = rong
        self.mau = color
        self.hop_le = dai > 0 and rong > 0

    def perimeter(self):
        if not self.hop_le:
            print("INVALID")
            exit()
        return 2 * (self.dai + self.rong)

    def area(self):
        return self.dai * self.rong

    def color(self):
        return self.mau.capitalize()
        

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
