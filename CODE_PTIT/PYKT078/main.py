import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        n = int(tokens[idx]); idx += 1
        m = int(tokens[idx]); idx += 1

        a = list(map(int, tokens[idx: idx + n])); idx += n
        khong_am = []
        am = []

        for x in a:
            if x < 0:
                am.append(x)
            else:
                khong_am.append(x)

        max_idx = 0
        for i in range(1, len(khong_am)):
            if khong_am[i] > khong_am[max_idx]:
                max_idx = i

        ans = am + khong_am[:max_idx] + [m] + khong_am[max_idx:]
        print(*ans)

if __name__ == "__main__":
    main()