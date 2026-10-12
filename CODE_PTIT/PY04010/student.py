class Student:
    def __init__(self, name, date, mon1, mon2, mon3, sum = 0.0):
        self.name = name
        self.date = date
        self.mon1 = mon1
        self.mon2 = mon2
        self.mon3 = mon3
        sum = mon1 + mon2 + mon3
        self.total = sum

    def __str__(self):
        return f"{self.name} {self.date} {self.total:.1f}"