from Point import point
from triangle import Triangle

def main():
    t = int(input())
    points = []

    for _ in range(t):
        points.extend(map(float, input().split()))

    idx = 0

    for _ in range(t):
        p1 = point(points[idx], points[idx + 1])
        p2 = point(points[idx + 2], points[idx + 3])
        p3 = point(points[idx + 4], points[idx + 5])

        triangle = Triangle(p1, p2, p3)

        result = triangle.perimeter()

        if result is None:
            print("INVALID")
        else:
            print(f"{result:.3f}")

        idx += 6


if __name__ == "__main__":
    main()