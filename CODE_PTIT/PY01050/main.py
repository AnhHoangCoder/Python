def Try(s, cntA, cntB, cntC, length):
    if len(s) == length:
        if cntA > 0 and cntB > 0 and cntC > 0 and cntA <= cntB <= cntC:
            print(s)
        return

    Try(s + 'A', cntA + 1, cntB, cntC, length)
    Try(s + 'B', cntA, cntB + 1, cntC, length)
    Try(s + 'C', cntA, cntB, cntC + 1, length)

def main():
    n = int(input().strip())
    for length in range(3, n + 1):
        Try("", 0, 0, 0, length)

if __name__ == "__main__":
    main()