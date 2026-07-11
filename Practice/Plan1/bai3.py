#Ma tran don vi

def identity_matrix(n):
    return [
        [1 if i == j else 0 for j in range(n)] for i in range(n)
    ]

n = int(input("Ma tran cap : "))
print(identity_matrix(n))