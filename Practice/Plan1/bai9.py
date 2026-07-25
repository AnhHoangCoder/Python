#send() vào generator: bộ tính tổng tích lũy python

def accumulator():
    total = 0
    while True:
        value = yield total
        total += value

t = int(input("Nhap so luong test case: "))
for _ in range(t):
    acc = accumulator()
    next(acc)

    s = input("Nhap so tich luy: ")
    arr = list(map(int, s.split()))

    for x in arr:
        print(acc.send(x))