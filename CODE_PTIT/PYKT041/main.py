def main():
    n = int(input().strip())
    a = [input().strip() for _ in range(n)]

    res = 0

    for i in range(n):
        k = a[i].count('C')
        res += k * (k - 1) // 2

    for j in range(n):
        k = 0
        for i in range(n):
            if a[i][j] == 'C':
                k += 1
        res += k * (k - 1) // 2

    print(res)

if __name__ == "__main__":
    main()