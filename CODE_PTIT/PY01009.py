# Cho một xâu ký tự chỉ bao gồm các ký tự chữ cái, độ dài không quá 100. Hãy thực hiện:

# Biến đổi tất cả xâu thành viết thường, nếu số lượng chữ cái viết thường lớn hơn hoặc bằng số lượng chữ cái viết hoa.
# Biến đổi tất cả xâu thành chữ hoa, nếu số lượng chữ cái viết hoa lớn hơn số lượng chữ cái viết thường.
# Input

# Chỉ có một xâu ký tự độ dài không quá 100, không có khoảng trống

# Output

# Ghi ra xâu kết quả

# Ví dụ

# Input

# Output

# vietHoa

	
# viethoa


# VIETTHuoNg

	
# VIETTHUONG

s = input()

lower = 0
upper = 0

for c in s:
    if c.islower():
        lower += 1
    else:
        upper += 1
print(s.lower() if lower >= upper else s.upper())