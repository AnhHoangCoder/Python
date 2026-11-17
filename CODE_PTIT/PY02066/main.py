import sys

def main():
    tokens = sys.stdin.buffer.read().split()

    n = int(tokens[0])
    a = list(map(int, tokens[1: 1 + n]))

    c = 0
    res = []
    for x in a:
        if c < x:
            c += 1
            while c < x:
                res.append(str(c))
                c += 1
        c = x

    if not res:
        print("Excellent!")
    else:
        print("\n".join(res))
        
if __name__ == "__main__":
    main()