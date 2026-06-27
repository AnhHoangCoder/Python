import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_up_to(n):
    # tra ve list cac so nguyen to <= n
    for i in range(2, n + 1, 1):
        if is_prime(i):
            print(i, end=" ")
    print()

n = int(input("Nhap so n = "))
primes_up_to(n)