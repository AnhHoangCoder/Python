from math import gcd

class Fraction:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        g = gcd(self.tu, self.mau)
        return Fraction(self.tu // g, self.mau // g)

    def __add__(self, other):
        tu = self.tu * other.mau + other.tu * self.mau
        mau = self.mau * other.mau
        return Fraction(tu, mau).rutGon()

    def __str__(self):
        return f"{self.tu}/{self.mau}"
    
a, b, c, d = map(int, input().split())
p = Fraction(a, b)
q = Fraction(c, d)

print(p + q)