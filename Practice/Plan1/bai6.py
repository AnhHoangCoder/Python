#Generator số chẵn trong khoảng

def even_range(start, stop):
    if start % 2 != 0:
        start += 1

    while start < stop:
        yield start
        start += 2

t = int(input("Nhap so test case: "))
for _ in range(t):
    start = int(input("Nhap start = "))
    stop = int(input("Nhap stop = "))
    print(list(even_range(start, stop)))