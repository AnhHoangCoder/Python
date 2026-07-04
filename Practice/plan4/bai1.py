#Tinh trung binh

def average(*nums):
    if(len(nums) == 0):
        return 0
    return (sum(nums) / len(nums))

n = int(input("Len: "))
a = []

for i in range(1, n + 1, 1):
    x = float(input(f"So thu {i} = "))
    a.append(x)

print(average(*a))
