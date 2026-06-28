#Loai trung lap, thu tu xuat hien dau tien

def dedupe_keep_order(lst):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return res

a = list(map(int, input().split()))

res = dedupe_keep_order(a)
print(res)
