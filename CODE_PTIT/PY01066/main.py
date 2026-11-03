def check(s1):
    s2 = s1[::-1]
    for i in range(1, len(s1)):
        if abs(ord(s1[i]) - ord(s1[i - 1])) != abs(ord(s2[i]) - ord(s2[i - 1])):
            return False
    return True

def main():
    res = []
    for _ in range(int(input().strip())):
        s = input()
        res.append("YES" if check(s) else "NO")
    print("\n".join(res))

if __name__ == "__main__":
    main()