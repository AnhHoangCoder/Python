#Kiem tra palindrome bang slicing

def is_palindrome(s):
    return s == s[::-1]

s = input("Nhap string: ")

if is_palindrome(s):
    print("True")
else:
    print("False")
