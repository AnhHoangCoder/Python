#In thong tin cua nhieu sinh vien

def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

students = []

n = int(input("Enter number of students: "))

for _ in range(n):
    student = {}
    student["name"] = input("Name: ")
    student["age"] = input("Age: ")
    student["school"] = input("School: ")

    students.append(student)

for student in students:
    print_info(**student)
    print("-" * 20)