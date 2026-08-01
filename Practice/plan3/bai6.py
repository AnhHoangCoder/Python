#Defaultdict: dem phan tu theo nhom

from collections import defaultdict

def group_words_by_length(words):
    #Giống với việc kiểm tra xem độ dài của word tồi tại chưa
    #Nếu chưa thì tạo 1 dict mới 
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)

    return dict(groups)

print(group_words_by_length(["cat", "dog", "elephant", "at", "is", "big"]))