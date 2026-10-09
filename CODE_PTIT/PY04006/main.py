from point import Point
from triangle import Triangle


def main():
    t = int(input())
    a = []

    for _ in range(t):
        a += [float(i) for i in input().split()]

    i = 0
    for _ in range(t):
        triangle = Triangle(
            Point(a[i], a[i + 1]),
            Point(a[i + 2], a[i + 3]),
            Point(a[i + 4], a[i + 5])
        )
        triangle.cnt()
        i += 6

if __name__ == "__main__":
    main()