class Matrix:
    def __init__(self, n, m, data = None):
        self.n, self.m = n, m
        self.data = [[0] * m for _ in range(n)] if data is None else [row[:] for row in data]

    def transpose(self):
        res = [[0] * self.n for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                res[i][j] = self.data[j][i]
        return Matrix(self.m, self.n, res)

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("Loi, ko khop nhan ma tran")
        res = [[0] * other.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    res[i][j] += (self.data[i][k] * other.data[k][j])
        return Matrix(self.n, other.m, res)
    
    def __str__(self):
        res = []
        for i in range(self.n):
            tmp = []
            for j in range(self.m):
                tmp.append(str(self.data[i][j]))

            res.append(" ".join(tmp))
        return "\n".join(res)