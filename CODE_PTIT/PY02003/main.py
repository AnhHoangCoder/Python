import sys
from bisect import bisect_left

def main():
    h = [1]
    i2 = i3 = i5 = 0

    MaxValue = 10**18
    while True:
        a = h[i2] * 2
        b = h[i3] * 3
        c = h[i5] * 5

        nxt = min(a, b, c)
        if nxt > MaxValue:
            break

        h.append(nxt)

        if nxt == a:
            i2 += 1

        if nxt == b:
            i3 += 1

        if nxt == c:
            i5 += 1
            
    tokens = sys.stdin.read().split()

    t = int(tokens[0])
    ans = []
    for i in range(1, t + 1):
        n = int(tokens[i])
        idx = bisect_left(h, n)

        if idx < len(h) and h[idx] == n:
            ans.append(str(idx + 1))
        else:
            ans.append("Not in sequence")
    print("\n".join(ans))

if __name__ == "__main__":
    main()