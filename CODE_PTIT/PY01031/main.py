import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    res = []
    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        n = int(tokens[idx]); idx += 1
        b = int(tokens[idx]); idx += 1

        if n == 0:
            res.append("0")
        else:
            s = ""
            while n > 0:
                s = digits[n % b] + s
                n //= b

            res.append(s)
    print("\n".join(res))

if __name__ == "__main__":
    main()