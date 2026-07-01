#Sap xep danh sach tuple theo diem giam dan

def sort_by_score_desc(a):
    return sorted(a, key=lambda t : t[1], reverse=True)

a = []
n = int(input())

for _ in range(n):
    key, value = input().split()
    a.append((key, int(value)))
print(sort_by_score_desc(a))