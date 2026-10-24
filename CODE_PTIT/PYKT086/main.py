DIGITS = "0123456789ABCDEF"

def transform(x, k):
    x = x.zfill(-(-len(x) // k) * k)
    return "".join(DIGITS[int(x[i:i + k], 2)] for i in range(0, len(x), k))

def main():
    with open("DATA.in", "r") as f:
        data = f.read().split()

    t = int(data[0])
    out = []
    for i in range(t):
        b = int(data[1 + 2 * i])
        x = data[2 + 2 * i]
        out.append(transform(x, b.bit_length() - 1))

    print("\n".join(out))

if __name__ == "__main__":
    main()