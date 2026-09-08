# Cho một dãy số A[] có 4 số nguyên dương, đánh số vị trí từ 1 đến 4. Tại mỗi bước, giá trị A[i] được thay thế bằng abs(A[i] – A[i+1]), riêng A[4] = abs(A[4]-A[1]).

# Hàm abs (trị tuyệt đối) được sử dụng để đảm bảo các giá trị của dãy số luôn dương.

 

# Hãy đếm xem sau bao nhiêu bước thì dãy số A[] có cả 4 vị trí đều bằng nhau.

 

# Input

# Có 4 số của dãy A[], các giá trị không quá 9 chữ số. Input kết thúc với 4 số 0.

# Output

# Với mỗi test, ghi ra số bước cần thực hiện.

# Ví dụ


# Input

# Output

# 1 3 5 9


# 4 3 2 1


# 0 0 0 0


	
# 6


# 4

import sys

def checkZero(a):
    return all(x == 0 for x in a)

def allEquals(a):
    return a[0] == a[1] == a[2] == a[3]

def main():
    data = sys.stdin.read().split()
    idx = 0
    res = []

    while True:
        a = list(map(int, data[idx: idx + 4])); idx += 4
        if checkZero(a):
            break

        step = 0
        while not allEquals(a):
            b = [0] * 4
            b[0] = abs(a[0] - a[1])
            b[1] = abs(a[1] - a[2])
            b[2] = abs(a[2] - a[3])
            b[3] = abs(a[3] - a[0])

            step += 1
            a = b

        res.append(str(step))
    print("\n".join(res))

if __name__ == "__main__":
    main()