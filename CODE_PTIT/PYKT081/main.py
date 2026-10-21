def main():
    res = []
    for _ in range(int(input().strip())):
        s = input().strip()
        a = s.split(".")

        if len(a) != 4:
            res.append("NO")
            continue

        flag = True

        for x in a:
            if not x.isdigit():
                flag = False
                break

            num = int(x)

            if num < 0 or num > 255:
                flag = False
                break

        res.append("YES" if flag else "NO")
    print("\n".join(res))

if __name__ == "__main__":
    main()