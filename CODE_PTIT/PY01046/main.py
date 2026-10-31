def hanoi(n, A, B, C):
    if n == 1:
        print(A, "->", C)
        return

    hanoi(n - 1, A, C, B)
    print(A, "->", C)
    hanoi(n - 1, B, A, C)

def main():
    n = int(input().strip())
    hanoi(n, 'A', 'B', 'C')

if __name__ == "__main__":
    main()