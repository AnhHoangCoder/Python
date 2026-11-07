def match(pattern, num):
    s = str(num)

    if len(s) != len(pattern):
        return False

    for x, y in zip(pattern, s):
        if x != '?' and x != y:
            return False

    return True

def solve(s):
    a, op, b, _, c = s.split()
    ops = ['+', '-', '*', '/']

    for x in range(10, 100):
        if not match(a, x):
            continue

        for y in range(10, 100):
            if not match(b, y):
                continue

            for o in ops:
                if op != '?' and op != o:
                    continue

                if o == '+':
                    res = x + y
                elif o == '-':
                    res = x - y
                elif o == '*':
                    res = x * y
                else:
                    if x % y != 0:
                        continue
                    res = x // y

                if 10 <= res < 100 and match(c, res):
                    return f"{x} {o} {y} = {res}"
    return "WRONG PROBLEM!"

def main():
    for _ in range(int(input().strip())):
        s = input()
        print(solve(s))
if __name__ == "__main__":
    main()