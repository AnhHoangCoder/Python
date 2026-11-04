import sys

def generate(n):
    res = []

    def Try(s, cnt, length):
        if(len(res) == n):
            return

        if(len(s) == length):
            if cnt * 2 > length:
                res.append(s)
            return

        for i in range(3):
            if len(res) == n:
                return

            ch = str(i)
            Try(s + ch, cnt + (i == 2), length)
    length = 1
    while len(res) < n:
        for i in range(1, 3):
            if len(res) == n:
                break
            Try(str(i), i == 2, length)
        length += 1
    return res
    
def main():
    tokens = sys.stdin.read().split()
    t = int(tokens[0])
    for i in range(1, t + 1):
        n = int(tokens[i])
        ans = generate(n)

        print(" ".join(ans[:n]))

if __name__ == "__main__":
    main()