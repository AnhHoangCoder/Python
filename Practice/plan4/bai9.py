#Itertools.groupby: Run-Length Encoding

from itertools import groupby

def run_length_encode(s):
    return [(key, len(list(group))) for key, group in groupby(s)]

def run_length_decode(encoded):
    return ''.join(char * count for char, count in encoded)

print(run_length_encode("aaabbbcc"))
print(run_length_encode("abcd"))
print(run_length_encode("aabbaaa"))

print(run_length_decode([('a',3),('b',2)]))
print(run_length_decode(run_length_encode("aaabbbcc")))