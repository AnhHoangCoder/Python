#Counter: Tim K ky tu xuat hien nhieu nhat

from collections import Counter

def top_k_chars(s, k):
    s = s.replace(" ", "")
    counter = Counter(s)
    # items = list(counter.items())
    # items.sort(key=lambda x: x[1], reverse=True)
    # return items[:k]
    return counter.most_common(k)

print(top_k_chars("banana split", 3))
print(top_k_chars("aabbcc", 2))