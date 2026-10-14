def main():
    s = input().strip()

    while len(s) % 3 != 0:
        s = '0' + s

    res = ''
    for i in range(0, len(s), 3):
        res += str(int(s[i: i + 3], 2))

    print(res)
if __name__ == "__main__":
    main()