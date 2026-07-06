#map() và filter() so với việc hiểu danh sách

def square_even_numbers(nums):
    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))

# def square_even_numbers(nums):
#     return [x * x for x in nums if x % 2 == 0]

n = int(input("Nhap so test case = "))
for _ in range(n):
    a = list(map(int, input().split()))
    print(square_even_numbers(a))
