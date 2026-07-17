#Ket qua cua bo nho dem trang tri(thu cong ghi nho)

def my_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@my_cache
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n-1) + fib_slow(n-2)

print(fib_slow(10))
print(fib_slow(35))