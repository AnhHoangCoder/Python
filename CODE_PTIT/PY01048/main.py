import sys
import math

def total(n):
    while n % 2 == 0:
        n //= 2
    cnt = 1
    for i in range(3, math.isqrt(n) + 1, 2):
        e = 0
        while n % i == 0:
            n //= i
            e += 1
        cnt *= (e + 1)
    if n > 1:
        cnt *= 2
    return cnt - 1 

def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    for i in range(1, t + 1):
        n = int(tokens[i])
        print(total(n))

if __name__ == "__main__":
    main()