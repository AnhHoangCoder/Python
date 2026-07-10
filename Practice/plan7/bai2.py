#Cay Fenwick

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1) # 1-indexed, bo index 0

    def update(self, i, delta):
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i) # lowbit: nhay len node cha

    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    
f = FenwickTree(5)

f.update(1, 3)
f.update(3, 5)
f.update(5, 2)

print(f.query(1))
print(f.query(2))
print(f.query(3))
print(f.query(5))