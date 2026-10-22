import sys


def FOR(a , b):
    return range(a, b + 1)

def main():
    score = {
        x: band
        for a, b, band in [
            (3, 4, 2.5), (5, 6, 3.0), (7, 9, 3.5),
            (10, 12, 4.0), (13, 15, 4.5), (16, 19, 5.0),
            (20, 22, 5.5), (23, 26, 6.0), (27, 29, 6.5),
            (30, 32, 7.0), (33, 34, 7.5), (35, 36, 8.0),
            (37, 38, 8.5), (39, 40, 9.0)
        ]
        for x in FOR(a, b)
    }

    tokens = sys.stdin.read().split()
    idx = 0

    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        r, l= map(int, tokens[idx: idx + 2]); idx += 2
        s, w = map(float, tokens[idx: idx + 2]); idx += 2

        avg = (score[r] + score[l] + s + w) / 4

        ans = int(avg * 2 + 0.50000001) / 2
        print(f"{ans:.1f}")

if __name__ == "__main__":
    main()