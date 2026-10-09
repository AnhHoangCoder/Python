from point import Point
import math

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def cnt(self):
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)

        if max(a, b, c) * 2 >= a + b + c:
            print("INVALID")
        else:
            d = math.sqrt(
                (a + b + c) *
                (a + b - c) *
                (a - b + c) *
                (-a + b + c)
            ) / 4
            print("{:.2f}".format(d))
            