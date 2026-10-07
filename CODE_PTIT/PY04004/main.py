from fraction import Fraction

a, b, c, d = map(int, input().split())
p = Fraction(a, b)
q = Fraction(c, d)

print(p + q)