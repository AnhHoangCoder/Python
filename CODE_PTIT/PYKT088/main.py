import math

def main():
    n = int(input().strip())

    s = math.isqrt(n)
    primes = [True] * (s + 1)
    primes[0] = False
    primes[1] = False

    for i in range(2, math.isqrt(s) + 1):
        if primes[i]:
            for j in range(i * i, s + 1, i):
                primes[j] = False

    # x ** 8 or (x**2) * (y**2)

    count = 0
    plist = [i for i in range(2, s + 1) if primes[i]]

    for p in plist:
        if p ** 8 > n:
            break

        count += 1

    m = len(plist)
    for i in range(m):
        p = plist[i]
        if i + 1 < m and p * plist[i + 1] > s:
            break
        for j in range(i + 1, m):
            q = plist[j]
            if p * q > s:
                break
            count += 1
        
    print(count)

if __name__ == "__main__":
    main()