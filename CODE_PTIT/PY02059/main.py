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

    ans = []
    maxValue = 0

    for i in range(n):
        row = list(map(int, tokens[idx: idx + m])); idx += m
        for j, x in enumerate(row):
            if isPrime(x):
                if x > maxValue:
                    maxValue = x
                    ans = [(i, j)]
                elif x == maxValue:
                    ans.append((i, j))
    if not ans:
        print("NOT FOUND")
    else:
        print(maxValue)
        for i, j in ans:
            print(f"Vi tri [{i}][{j}]")

if __name__ == "__main__":
    main()