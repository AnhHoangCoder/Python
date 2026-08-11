#So hoc & lam tron

def division_info(a, b):
    result = {
        "quotient": a // b,
        "remainder": a % b,
        "float_div": a / b,
        "rounded": round(a / b),
        "floor": math.floor(a / b),
        "ceil": math.ceil(a / b)
    }
    return result

import math

t = int(input("Nhap so test case = "))
for _ in range(t):
    print("Nhap 2 so a va b")

    a = int(input("Nhap so a = "))
    b = int(input("Nhap so b = "))

    result = division_info(a, b)
    print(result["quotient"])
    print(result["remainder"])
    print(result["float_div"])
    print(result["rounded"])
    print(result["floor"])
    print(result["ceil"])