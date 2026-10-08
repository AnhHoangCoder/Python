import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def perimeter(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)

        if max(a, b, c) * 2 >= a + b + c:
            return None

        return a + b + c

t = int(input())

points = []

for _ in range(t):
    points.extend(map(float, input().split()))

idx = 0

for _ in range(t):
    p1 = Point(points[idx], points[idx + 1])
    p2 = Point(points[idx + 2], points[idx + 3])
    p3 = Point(points[idx + 4], points[idx + 5])

    triangle = Triangle(p1, p2, p3)

    result = triangle.perimeter()

    if result is None:
        print("INVALID")
    else:
        print(f"{result:.3f}")

    idx += 6