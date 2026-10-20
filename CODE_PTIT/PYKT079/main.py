import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    res = []
    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        n = int(tokens[idx]); idx += 1
        a = list(map(int, tokens[idx: idx + n])); idx += n

        a.sort()
        minValue, maxValue = a[0], a[n - 1]

        count = maxValue - minValue + 1 - len(set(a))
        res.append(str(count))
    print("\n".join(res))
        

if __name__ == "__main__":
    main()