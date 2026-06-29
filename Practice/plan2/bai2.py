#Đếm tần suất từ trong câu

from collections import Counter

# def wordFreq(s):
#     words = s.lower().split()

#     return Counter(words)

# s = input()
# cnt = wordFreq(s)
# for word, freq in cnt.items():
#     print(word, freq)

def wordFreq(s):
    words = s.lower().split()
    return Counter(words)

s = input()
print(wordFreq(s))