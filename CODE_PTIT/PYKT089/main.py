import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    n = int(tokens[idx]); idx += 1
    a = list(map(int, tokens[idx : idx + n])); idx += n

    chan = []
    le = []

    idx_chan = []
    idx_le = []

    for i in range(n):
        if a[i] % 2 == 0:
            chan.append(a[i])
            idx_chan.append(i)
        else:
            le.append(a[i])
            idx_le.append(i)

    chan.sort()
    le.sort(reverse=True)

    i, j = 0, 0
    for x in chan:
        a[idx_chan[i]] = x
        i += 1

    for x in le:
        a[idx_le[j]] = x
        j += 1

    print(*a)
if __name__ == "__main__":
    main()