import sys

tokens = sys.stdin.read().split()
idx = 0

n = int(tokens[idx]); idx += 1
k = int(tokens[idx]); idx += 1

a = list(map(int, tokens[idx: idx + n])); idx += n

a = sorted(set(a))

if k > len(a):
    exit()

res = []

def Try(start):
    if len(res) == k:
        print(*res)
        return

    for i in range(start, len(a)):
        res.append(a[i])
        Try(i + 1)
        res.pop()

def main():
    Try(0)

if __name__ == "__main__":
    main()