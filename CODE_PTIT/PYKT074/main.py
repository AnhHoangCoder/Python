def main():
    t = int(input().strip())
    ans = []
    for _ in range(t):
        s = input().strip()
        words = s.split()
        res = ""

        for w in words:
            if res == "":
                new_len = len(w)
            else:
                new_len = len(res) + 1 + len(w)

            if new_len > 100:
                break

            res = w if res == "" else res + " " + w
        ans.append(res)
    print("\n".join(ans))

if __name__ == '__main__':
    main()