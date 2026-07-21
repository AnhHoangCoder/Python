#Thu vien co so thong ke ko su dung

def statistics(nums):
    s = sorted(nums)
    n = len(s)

    return {
        "min": min(nums),
        "max": max(nums),
        "mean": sum(nums)/n,
        "median": s[n//2] if n % 2 else (s[n//2 - 1] + s[n//2])/2
    }

t = int(input("Nhap test case: "))
for i in range(1, t+1):
    print(f"test case so {i}")
    s = input("Nhap so phan tu: ")
    nums = list(map(int, s.split()))
    print(statistics(nums))
