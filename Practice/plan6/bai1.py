#Class stack dung list

class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, x):
        self.data.append(x)

    def pop(self):
        if self.is_empty():
            return None
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    
s = Stack()

print(s.is_empty())

n = int(input(("Nhap so phan tu can push = ")))
for _ in range(n):
    x = int(input())
    s.push(x)

while not s.is_empty():
    print(s.peek())
    s.pop()

print(s.is_empty())