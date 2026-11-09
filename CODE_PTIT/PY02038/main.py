def main():
    n = int(input().strip())

    row = [0] * n
    col = [0] * n
    for i in range(n):
        s = input().strip()
        for j in range(n):
            if s[j] == 'C':
                row[i] += 1
                col[j] += 1

    ans = 0

    for x in row:
        ans += x * (x - 1) // 2

    for x in col:
        ans += x * (x - 1) // 2

    print(ans)

if __name__ == "__main__":
    main()