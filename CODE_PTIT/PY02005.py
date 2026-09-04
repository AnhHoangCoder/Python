# Cho dãy số A[] gồm có N phần tử.

# Một cặp nghịch thế là một cặp số (u, v) sao cho u < v và A[u] > A[v]. Nhiệm vụ của bạn là hãy đếm số lượng cặp nghịch thế trong dãy số A[] ban đầu.

# Input:

# Dòng đầu tiên là N (N ≤ 1000), số lượng phần tử trong dãy số ban đầu.

# Dòng tiếp theo gồm N số nguyên A[i] (1 ≤ A[i] ≤ 109).

# Output: 

# In ra một số nguyên là số lượng dãy nghịch thế tìm được.

# Ví dụ:


# Input:

# Output

# 5


# 2 4 1 3 5


	
# 3

def merge_count(a):
    n = len(a)
    if n <= 1:
        return a, 0
    mid = n // 2
    left, count_left = merge_count(a[:mid])
    right, count_right = merge_count(a[mid:])

    merged = []
    i = j = 0
    count_split = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            count_split += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count_left + count_split + count_right

def main():
    n = int(input())
    a = list(map(int, input().split()))
    _, count = merge_count(a)
    print(count)

if __name__ == "__main__":
    main()