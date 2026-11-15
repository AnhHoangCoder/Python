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

    n, m = map(int, tokens[idx: idx + 2]); idx += 2

    a = []
    ans = []
    maxValue = 0

    for _ in range(n):
        row = list(map(int, tokens[idx: idx + m])); idx += m
        for x in row:
            if isPrime(x):
                maxValue = max(maxValue, x)
        a.append(row)

    for i in range(n):
        for j in range(m):
            if a[i][j] == maxValue:
                ans.append((i , j))

    if maxValue == 0:
        print("NOT FOUND")
        return
    print(maxValue)
    for x in ans:
        print(f"Vi tri [{x[0]}][{x[1]}]")
    
if __name__ == "__main__":
    main()