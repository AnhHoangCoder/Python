#Bài này yêu cầu viết 3 generator nhỏ rồi nối nhau thành pipeline

def read_numbers(filepath):
    with open(filepath, "r") as f:
        for line in f:
            yield int(line.strip())

def filter_positive(numbers):
    for num in numbers:
        if num > 0:
            yield num

def square(numbers):
    for num in numbers:
        yield num * num

with open("nums.txt", "w") as f:
    f.write("3\n-1\n4\n-2\n5\n0\n2\n")

pipeline = square(filter_positive(read_numbers("nums.txt")))
print(list(pipeline))