def main():
    t = int(input().strip())
    res = []
    count7 = 0
    in_luc_bat = False

    for _ in range(t):
        k = len(input().split())

        if k == 7:
            count7 += 1
            in_luc_bat = False

            if count7 == 4:
                res.append("2")
                count7 = 0

        elif k == 6:
            count7 = 0
            if not in_luc_bat:
                res.append("1")
                in_luc_bat = True
                
        elif k == 8:
            count7 = 0

    print(len(res))
    print("\n".join(res))
if __name__ == "__main__":
    main()