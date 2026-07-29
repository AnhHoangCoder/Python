#Decorator log tham so va ket qua

def log_call(func):
    def wrapper(*args, **kwargs):
        args_str = ", ".join(map(str, args))

        kwargs_str = ", ".join(f"{k}={v}" for k, v in kwargs.items())

        if args_str and kwargs_str:
            all_args = args_str + ", " + kwargs_str
        else:
            all_args = args_str or kwargs_str

        result = func(*args, **kwargs)

        print(f"[LOG] {func.__name__}({all_args}) -> {result}")

        return result
    return wrapper

@log_call
def multiply(a, b):
    return a * b

multiply(3, 4)
multiply(a=5, b=2)