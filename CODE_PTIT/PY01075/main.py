import sys
from math import gcd

def solve(tokens, idx):
    n = int(tokens[idx])
    idx += 1

    a = list(map(int, tokens[idx:idx+n]))
    idx += n

    c = list(map(int, tokens[idx:idx+n]))
    idx += n

    dp = {}

    for i in range(n):
        ndp = dp.copy()
        ndp[a[i]] = min(ndp.get(a[i], float('inf')), c[i])

        for g, cost in dp.items():
            ng = gcd(g, a[i])
            nc = cost + c[i]
            ndp[ng] = min(ndp.get(ng, float('inf')), nc)

        dp = ndp

    return dp.get(1, -1), idx


def main():
    tokens = sys.stdin.read().split()
    idx = 0

    t = int(tokens[idx])
    idx += 1

    for _ in range(t):
        ans, idx = solve(tokens, idx)
        print(ans)


if __name__ == "__main__":
    main()