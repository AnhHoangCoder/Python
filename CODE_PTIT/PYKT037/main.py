def main():
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for _ in range(int(input())):
        n, b = map(int, input().split())
        res = ""
        while n > 0:
            res += digits[n % b]
            n //= b
        print(res[::-1])

if __name__ == "__main__":
    main()