import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    n, m = map(int, tokens[idx: idx + 2]); idx += 2

    a = []
    for _ in range(n):
        row = list(map(int, tokens[idx: idx + m])); idx += m
        a.append(row)

    if n > m:
        d = n - m
        idx = [i for i in range(n) if not (i % 2 == 0 and i < 2 * d)]
        a = [a[i] for i in idx]
    elif m > n:
        d = m - n
        idx = [j for j in range(m) if not (j % 2 == 1 and j < 2 * d)]
        a = [[row[j] for j in idx] for row in a]

    for row in a:
        print(*row)
if __name__ == "__main__":
    main()