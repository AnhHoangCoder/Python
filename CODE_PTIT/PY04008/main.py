import sys

from matrix import Matrix

def main():
    tokens = sys.stdin.read().split()
    idx = 0

    t = int(tokens[idx]); idx += 1
    for _ in range(t):
        n = int(tokens[idx]); idx += 1
        m = int(tokens[idx]); idx += 1
        data = []

        for _ in range(n):
            tmp = list(map(int, tokens[idx : idx + m])); idx += m
            data.append(tmp)

        a = Matrix(n, m , data)
        b = a.transpose()

        print(a * b)

if __name__ == "__main__":
    main()