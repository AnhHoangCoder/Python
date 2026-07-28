#Decorator retry khi gap loi

import random

def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_err = None

            for attempt in range(times):
                try:
                    print(f"Thử lần {attempt + 1}")
                    return func(*args, **kwargs)
                except Exception as e:
                    print("Lỗi:", e)
                    last_err = e
            raise last_err
        return wrapper
    return decorator

n = int(input("Nhập số lần thử: "))
p = float(input("Nhập xác suất lỗi (0-1): "))

@retry(times=n)
def unstable_api():
    if random.random() < p:
        raise ConnectionError("Mất kết nối!")
    return "Thành công!"

result = unstable_api()
print(result)