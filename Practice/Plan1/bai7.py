#Trình tạo số nguyên tố vô hạn

def is_prime(n)->bool:
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def infinite_primes():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1

import itertools

gen = infinite_primes()

print(list(itertools.islice(gen, 5)))
print(list(itertools.islice(gen, 5)))

gen2 = infinite_primes()
print(list(itertools.islice(gen2, 20))[-1])