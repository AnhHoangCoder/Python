# Trong 10 chữ số thập phân thì có 4 chữ số nguyên tố là 2, 3, 5, 7.

# Một số nguyên dương được coi là thỏa mãn nguyên tố đúng vị trí nếu thỏa mãn cả hai điều kiện:

# Nếu i là nguyên tố thì vị trí thứ i cũng phải là chữ số nguyên tố.
# Ngược lại nếu i không phải là số nguyên tố thì vị trí thứ i không phải là chữ số nguyên tố. 
# Ví dụ: số 14239567 thỏa mãn nguyên tố đúng vị trí vì các vị trí thứ 2, 3, 5, 7 là các chữ số nguyên tố, các vị trí khác không nguyên tố. 

# Viết chương trình kiểm tra một số nguyên dương không quá 500 chữ số có thỏa mãn tính chất trên hay không. 

# Input

# Dòng đầu ghi số bộ test, không quá 10.

# Mỗi bộ test viết trên một dòng số nguyên dương không quá 500 chữ số.

# Output

# Với mỗi test, ghi ra YES hoặc NO tùy thuộc kết quả kiểm tra

# Ví dụ


# Input

# Output

# 2


# 14239567


# 2314514535353


	
# YES


# NO

import math

def is_prime(n : int) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def check(s) -> bool:
    for i in range(0, len(s)):
        t = int(s[i])
        if is_prime(i):
            if not is_prime(t):
                return False
        else:
            if is_prime(t):
                return False
    return True

def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print("YES" if check(s) else "NO")

if __name__ == "__main__":
    main()