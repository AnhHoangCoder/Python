from student import Student

def main():
    name = input().strip()
    date = input().strip()
    mon1 = float(input())
    mon2 = float(input())
    mon3 = float(input())

    print(Student(name, date, mon1, mon2, mon3))

if __name__ == "__main__":
    main()