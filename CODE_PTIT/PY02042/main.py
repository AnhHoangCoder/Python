def Sub(a : str, b : str):
    a = a.lstrip('0') or '0'
    b = b.lstrip('0') or '0'

    sign = ''

    if len(a) < len(b) or (len(a) == len(b) and a < b):
        a, b = b, a
        sign = '-'

    a = a[::-1]
    b = b[::-1]

    l = max(len(a), len(b))
    tmp = 0
    ans = []

    for i in range(l):
        x = int(a[i])
        y = int(b[i]) if i < len(b) else 0

        sub = x - y - tmp
        if sub < 0:
            sub += 10
            tmp = 1
        else:
            tmp = 0

        ans.append(str(sub))
    res = ''.join(ans[::-1]).lstrip('0') or '0'

    if res == '0':
        return '0'

    return sign + res

def main():
    a = input().strip()
    b = input().strip()

    print(Sub(a, b))

if __name__ == "__main__":
    main()