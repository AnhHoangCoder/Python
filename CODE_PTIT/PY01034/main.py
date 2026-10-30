import sys

def solve(s):
    n = len(s)
    cnt = [0] * 10
    cnt[int(s[-1])] += 1
    for i in range(n - 2, -1, -1):
        c = int(s[i])
        lo = 1 if i == 0 else 0
        for d in range(c - 1, lo - 1, -1):
            if cnt[d]:
                j = s.index(str(d), i + 1)
                l = list(s)
                l[i], l[j] = l[j], l[i]
                return "".join(l)
        cnt[c] += 1
    return "-1"

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    for k in range(1, t + 1):
        print(solve(tokens[k]))

if __name__ == "__main__":
    main()