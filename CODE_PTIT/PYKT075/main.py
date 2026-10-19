from pathlib import Path

def sort_key(contact):
    name = contact[0]
    parts = name.split()
    return (parts[-1], " ".join(parts[:-1]))

def main():
    folder = Path(__file__).parent
    input_file = folder / "SOTAY.txt"
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    res = []
    i = 0
    day_now = ""
    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("Ngay"):
            day_now = line[5:].strip()
            i += 1
        else:
            name = lines[i].strip()
            phone = lines[i + 1].strip()
            res.append((name, phone, day_now))
            i += 2

    res.sort(key= sort_key)
    output = []
    for name, phone, day in res:
        output.append(f"{name}: {phone} {day}")

    output_file = folder / "DIENTHOAI.txt"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    main()