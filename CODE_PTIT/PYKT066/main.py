import sys
import math

def main():
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx]); idx += 1
    for _ in range(t):
        n = int(data[idx]); idx += 1
        k = int(data[idx]); idx += 1

        a = list(map(int, data[idx: idx + n])); idx += n

        ans = n + 1
        prev = []

        for x in a:
            cur = [(x, 1)]
            for g, length in prev:
                ng = math.gcd(x, g)

                if cur[-1][0] == ng:
                    cur[-1] = (ng, min(cur[-1][1], length + 1))
                else:
                    cur.append((ng, length + 1))

            for g, length in cur:
                if g == k:
                    ans = min(ans, length)
            prev = cur

        print(ans if ans <= n else -1)
if __name__ == "__main__":
    main()