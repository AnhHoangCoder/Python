import sys

def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    s = data[1:1 + n]

    best = -1
    base = s[0]
    L = len(base)

    for i in range(L):
        target = base[i:] + base[:i]
        total = 0
        ok = True
        for x in s:
            pos = (x + x).find(target)
            if pos == -1:
                ok = False
                break
            total += pos
        if ok and (best == -1 or total < best):
            best = total

    print(best)

main()