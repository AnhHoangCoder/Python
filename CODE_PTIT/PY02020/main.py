import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(float, data[1:n + 1]))

    lo, hi = min(a), max(a)
    scores = [x for x in a if x != lo and x != hi]

    print(f"{sum(scores) / len(scores):.2f}")

if __name__ == "__main__":
    main()