class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        Real = self.real + other.real
        Imag = self.imag + other.imag
        return Complex(Real, Imag)

    def __mul__(self, other):
        Real = self.real * other.real - self.imag * other.imag
        Imag = self.real * other.imag + self.imag * other.real
        return Complex(Real, Imag)

    def __str__(self):
        s = str(self.real)
        c = " + "
        if(self.imag < 0):
            c = " - "
        s += c
        s += f"{abs(self.imag)}i"
        return s

def main():
    res = []
    for _ in range(int(input())):
        a1, a2, b1, b2 = list(map(int, input().split()))
        a = Complex(a1, a2)
        b = Complex(b1, b2)

        c = (a + b) * a
        d = (a + b) * (a + b)

        res.append(f"{c}, {d}")
    print("\n".join(res))

if __name__ == "__main__":
    main()