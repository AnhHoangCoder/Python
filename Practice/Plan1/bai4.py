#Lam phang(flatten) list 2 chieu

def flatten(matrix):
    return [x for row in matrix for x in row]

print(flatten([[1,2,3],[4,5],[6]]))
print(flatten([[]]))
print(flatten([[1],[2],[3]]))