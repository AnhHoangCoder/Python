import sys

Digits = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def solve(n, k):
    while n > 1:
        mid = 1 << (n - 1)
        if k == mid:
            return Digits[n - 1]
        elif k > mid:
            k -= mid

        n -= 1
    return Digits[0]

def main():
    tokens = sys.stdin.read().split()
    idx = 0
    res = []
    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        n = int(tokens[idx]); idx += 1
        k = int(tokens[idx]); idx += 1
        res.append(solve(n, k))
    print("\n".join(res))


if __name__ == "__main__":
    main()