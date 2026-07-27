#Decorator giới hạn số lần gọi

def max_calls(n):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= n:
                raise Exception(f"Hàm chỉ được gọi tối đa {n} lần!")
            count += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@max_calls(3)
def greet(name):
    return f"Xin chào {name}!"

print(greet("An"))
print(greet("Binh"))
print(greet("Cuong"))
print(greet("Dung"))