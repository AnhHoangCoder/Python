##Ep kieu & kiem tra kieu

def type_info(val): 
    #Ep kieu int
    try:
        as_int = int(val)
    except (ValueError, TypeError):
        as_int = None
    #Ep kieu float
    try:
        as_float = float(val)
    except (ValueError, TypeError):
        as_float = None
    #Ep kieu bool
    as_bool = bool(val)

    return {
        "value": val,
        "type": type(val).__name__,
        "as_int": as_int,
        "as_float": as_float,
        "as_bool": as_bool
    }

print(type_info(3.7))

# Test
assert type_info(3.7) == {
    "value": 3.7,
    "type": "float",
    "as_int": 3,
    "as_float": 3.7,
    "as_bool": True
}

assert type_info("42") == {
    "value": "42",
    "type": "str",
    "as_int": 42,
    "as_float": 42.0,
    "as_bool": True
}

assert type_info("abc") == {
    "value": "abc",
    "type": "str",
    "as_int": None,
    "as_float": None,
    "as_bool": True
}

assert type_info(0) == {
    "value": 0,
    "type": "int",
    "as_int": 0,
    "as_float": 0.0,
    "as_bool": False
}

print("Tất cả test đều PASS")