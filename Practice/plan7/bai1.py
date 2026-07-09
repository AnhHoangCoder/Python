#Hop tap hop roi rac(DSU)

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)

        if px != py:
            self.parent[py] = px

d = DSU(5)

print(d.find(0) == d.find(1))

d.union(0, 1)
print(d.find(0) == d.find(1))

d.union(1, 2)
print(d.find(0) == d.find(2))

print(d.find(3) == d.find(4))