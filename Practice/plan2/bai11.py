#Decorator kiem tra dau vao du lieu

def validate_types(*types):
    def decorator(func):
        def wrapper(*args, **kwargs):

            for i, (arg, expected) in enumerate(zip(args, types)):
                if not isinstance(arg, expected):
                    raise TypeError(
                        f"Tham số {i}: cần {expected.__name__}, nhận {type(arg).__name__}"
                    )

            return func(*args, **kwargs)

        return wrapper
    return decorator


@validate_types(int, int)
def add(a, b):
    return a + b


print(add(1, 2))
print(add(1.5, 2))