import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0
    n = int(tokens[idx]); idx += 1
    k = int(tokens[idx]); idx += 1

    a = list(map(int, tokens[idx: idx + n]))
    a.sort()

    cnt = 1
    for i in range(1, n):
        if a[i] - a[i - 1] > k:
            cnt += 1

    print(cnt)

if __name__ == "__main__":
    main()