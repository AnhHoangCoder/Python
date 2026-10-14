import sys

def check(a, b):
    n = len(a)
    for i in range(n):
        if a[i] > b[i]:
            return False
    return True

def main():
    data = sys.stdin.read().split()
    idx = 0

    t = int(data[idx]); idx += 1
    res = []
    for _ in range(t):
        n = int(data[idx]); idx += 1
        a = list(map(int, data[idx : idx + n])); idx += n
        b = list(map(int, data[idx : idx + n])); idx += n

        a.sort()
        b.sort()

        res.append("YES" if check(a, b) else "NO")
    print("\n".join(res))


if __name__ == "__main__":
    main()