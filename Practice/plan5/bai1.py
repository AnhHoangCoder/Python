#Chia 2 so bat loi rieng biet

def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        return a / b
    
    except ZeroDivisionError:
        return "Error: chia cho 0"
    
    except ValueError:
        return "Error: ko phai so"

n = int(input("Nhap so test case = "))
for _ in range(n):
    a = input("Nhap a = ")
    b = input("Nhap b = ")
    print(safe_divide(a, b))