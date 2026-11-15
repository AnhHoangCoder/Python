import sys

def isPalindrome(n):
    s = str(n)
    return len(s) >= 2 and s == s[::-1]

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    n, m = map(int, tokens[idx: idx + 2]); idx += 2

    maxValue = 0
    ans = []

    for i in range(n):
        row = list(map(int, tokens[idx: idx + m])); idx += m
        for j, x in enumerate(row):
            if isPalindrome(x):
                if x > maxValue:
                    maxValue = x
                    ans = [(i, j)]
                elif x == maxValue:
                    ans.append((i, j))

    if maxValue == 0:
        print("NOT FOUND")
    else:
        print(maxValue)
        for i, j in ans:
            print(f"Vi tri [{i}][{j}]")

if __name__ == "__main__":
    main()