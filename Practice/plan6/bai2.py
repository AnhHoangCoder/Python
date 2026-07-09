#Class sinh vien co the sorted truc tiep

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name}: {self.score}"

    def __lt__(self, other):
        return self.score < other.score

a = Student("An", 7)
b = Student("Binh", 9)

print(str(a))
print(a < b)

students = [b, a]
students = sorted(students)

for s in students:
    print(s)