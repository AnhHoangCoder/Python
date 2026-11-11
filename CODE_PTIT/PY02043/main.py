def countInString(a : str, b : str) -> int:
    ans = 0
    i = 0
    n = len(a)
    m = len(b)

    while i <= n - m:
        if a[i: i+m] == b:
            ans += 1
            i += m
        else:
            i += 1

    return ans

def main():
    for _ in range(int(input().strip())):
        a = input().strip()
        b = input().strip()
        print(countInString(a, b))

if __name__ == "__main__":
    main()
