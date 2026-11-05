n = int(input())
digits = "2357"

def Try(s, mask, length):
    if len(s) == length:
        if mask == 15 and s[-1] in "357":
            print(s)
        return

    for i in range(4):
        x = digits[i]
        Try(s + x, mask | (1 << i), length)

def main():
    for length in range(4, n + 1):
        Try("", 0, length)

if __name__ == "__main__":
    main()
