import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        n = int(tokens[idx]); idx += 1
        a = list(map(int, tokens[idx: idx + n])); idx += n

        dp = [0] * n

        for i in range(n):
            j = i - 1

            while j >= 0 and a[j] <= a[i]:
                j -= dp[j]

            dp[i] = i - j
            
        print(*dp)

if __name__ == "__main__":
    main()
