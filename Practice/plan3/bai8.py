#Namedtuple: Ban ghi sinh vien

from collections import namedtuple

Student = namedtuple("Student", ["ten", "diem", "lop"])

def top_students(students, n):
    return sorted(
        students,
        key=lambda s: s.diem,
        reverse=True
    )[:n]

ds = [
    Student("An", 8.5, "A"),
    Student("Binh", 9.0, "B"),
    Student("Chi", 7.5, "A"),
    Student("Dat", 9.5, "B"),
]

print(top_students(ds, 2))