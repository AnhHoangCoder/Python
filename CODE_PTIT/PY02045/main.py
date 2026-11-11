def Total(s):
    mid = len(s) // 2
    return int(s[:mid]) + int(s[mid:])

def main():
    s = input().strip()
    while len(s) > 1:
        s = str(Total(s))
        print(s)

if __name__ == "__main__":
    main()