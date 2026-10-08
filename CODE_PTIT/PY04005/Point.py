import math

class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        dx = other.x - self.x
        dy = other.y - self.y

        return math.sqrt(dx ** 2 + dy ** 2)