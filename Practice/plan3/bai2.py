#Cac tu dao nguoc trong cau

def reverse_words(sentence):
    res = " ".join(reversed(sentence.split()))
    return res

sentence = input("Nhap string = ")
print(reverse_words(sentence))