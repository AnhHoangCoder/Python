from complex import Complex

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