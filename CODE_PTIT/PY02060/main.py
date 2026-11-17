
import sys

def main():
    MOD = 10**9 + 7

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    tests = [(data[i], data[i+1]) for i in range(1, 2*t+1, 2)]

    limit = max(b for a, b in tests)

    spf = list(range(limit + 1))

    for i in range(2, int(limit**0.5) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i

    primes = [i for i in range(2, limit + 1) if spf[i] == i]

    for a, b in tests:
        ans = 1

        for p in primes:
            if p > b:
                break

            k = 0
            power = p

            while power <= b:
                k += b // power - (a - 1) // power
                power *= p

            if k:
                ans = ans * (2 * k + 1) % MOD

        print(ans)
if __name__ == "__main__":
    main()
