#Generator & Iterator(Python-only)

import itertools

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci()
print([next(gen) for _ in range(7)])

gen2 = fibonacci()
print(list(itertools.islice(gen2, 10)))
