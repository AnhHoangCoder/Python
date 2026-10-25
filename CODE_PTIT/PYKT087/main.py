import sys

mod = 10**9 + 7

def sdb(n , k):
    cur = 1
    ans = 0

    while k > 0:
        if k & 1:
            ans = (ans + cur) % mod
        cur = cur * n % mod
        k >>= 1
    return ans

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])

    res = []
    for i in range(t):
        n = int(tokens[1 + 2*i])
        k = int(tokens[2 + 2*i])

        res.append(sdb(n, k))
    print("\n".join(map(str, res)))

if __name__ == "__main__":
    main()