import sys

def isPrime(n : int) -> bool:
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    n = int(tokens[idx]); idx += 1
    a = list(map(int, tokens[idx: idx + n]))

    b = []
    for x in a:
        if not x in b:
            b.append(x)

    m = len(b)
    dp = [0] * m
    dp[0] = b[0]
    for i in range(1, m):
        dp[i] = dp[i - 1] + b[i]

    idx = -1

    for i in range(m):
        if isPrime(dp[i]) and isPrime(dp[m-1] - dp[i]):
            idx = i
            break

    print(idx if idx != -1 else "NOT FOUND")

if __name__ == "__main__":
    main()