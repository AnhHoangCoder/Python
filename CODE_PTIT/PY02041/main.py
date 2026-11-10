def Sum(a : str, b : str):
    a = a[::-1]
    b = b[::-1]

    l = max(len(a), len(b))
    tmp = 0
    ans = ""
    for i in range(l):
        num1 = int(a[i]) if i < len(a) else 0
        num2 = int(b[i]) if i < len(b) else 0

        total = num1 + num2 + tmp
        if total >= 10:
            total -= 10
            tmp = 1
        else:
            tmp = 0        

        ans += str(total)

    if tmp > 0:
        ans += str(tmp)

    j = len(ans) - 1
    while ans[j] == '0' and j > 0:
        j -= 1
    res = ans[:j+1]
    return res[::-1]

def main():
    a = input().strip()
    b = input().strip()

    print(Sum(a, b))
if __name__ == "__main__":
    main()