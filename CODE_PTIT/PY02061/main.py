import sys

def main():
    tokens = sys.stdin.buffer.read().split()

    t = int(tokens[0])
    idx = 1

    for _ in range(t):
        n, m = map(int, tokens[idx: idx + 2]); idx += 2
        x = []
        for _ in range(n):
            x.append(list(map(int, tokens[idx: idx + m])))
            idx += m

        h = []
        for _ in range(3):
            h.append(list(map(int, tokens[idx: idx + 3])))
            idx += 3

        u, v = n - 2, m - 2

        total = 0
        for i in range(u):
            for j in range(v):
                for a in range(3):
                    for b in range(3):
                        total += x[i + a][j + b] * h[a][b]

        print(total)

if __name__ == "__main__":
    main()