#Doc va xu li thu cong CSV

def parse_csv(filepath):
    result = []

    with open(filepath, "r") as f:
        lines = f.readlines()

        header = lines[0].strip().split(",")

        for line in lines[1:]:
            row = line.strip().split(",")

            student = dict(zip(header, row))

            result.append(student)

    return result

with open("students.csv", "w") as f:
    f.write("ten,diem,lop\n")
    f.write("An,8,A\n")
    f.write("Binh,7,B\n")
    f.write("Chi,9,A\n")

print(parse_csv("students.csv"))