#Generator doc lon tung dong file

def read_lines(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()
    
with open("test.txt", "w") as f:
    f.write("   dong mot   \n   dong hai   \n   dong ba \n")
    
gen = read_lines("test.txt")

print(next(gen))
print(next(gen))
print(next(gen))