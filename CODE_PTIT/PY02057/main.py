import sys

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    n, m = map(int, tokens[idx: idx + 2]); idx += 2

    a = []
    maxValue = 0
    minValue = 10001
    distance = 0

    ans = []
    for i in range(n):
        row = list(map(int, tokens[idx: idx + m])); idx += m
        a.append(row)
        maxValue = max(maxValue,max(row))
        minValue = min(minValue, min(row))

    distance = maxValue - minValue

    for i in range(n):
        for j in range(m):
            if a[i][j] == distance:
                ans.append((i, j))

    if not ans:
        print("NOT FOUND")
    else:
        print(distance)
        for i, j in ans:
            print(f"Vi tri [{i}][{j}]")

    
if __name__ == '__main__':
    main()