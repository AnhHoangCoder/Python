import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    res = []
    t = int(tokens[idx])
    idx += 1
    for _ in range(t):
        n, p = map(int, tokens[idx: idx + 2])
        idx += 2

        if n < p:
            res.append("0")
            continue

        count = 0

        x = 1
        while p * x <= n:
            count += 1
            if x % p == 0:
                tmp = x
                while tmp % p == 0:
                    count += 1
                    tmp //= p
            x += 1

        res.append(str(count))
    print("\n".join(res))    

if __name__ == "__main__":
    main()