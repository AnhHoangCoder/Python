def generate(a, k):
    res = []
    l = len(a)
    b = []

    def Try(start):
        if len(b) == k:
            res.append(" ".join(b))
            return

        for i in range(start, l):
            b.append(a[i])
            Try(i + 1)
            b.pop()

    Try(0)
    return "\n".join(res)

def main():
    n, k = map(int, input().split())
    a = list(set(input().split()))

    a.sort()
    print(generate(a, k))

if __name__ == "__main__":
    main()