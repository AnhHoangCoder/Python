#deque: queue co limit size(sliding window)

from collections import deque

def sliding_window_max(nums, k):
    dq = deque()
    ans = []

    for i in range(len(nums)):
        #Loại index đã ra khỏi cửa sổ
        while dq and dq[0] <= i - k:
            dq.popleft()

        #Loại các phần tử nhỏ hơn phần tử mới
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            ans.append(nums[dq[0]])

    return ans

print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))

print(sliding_window_max([1,2,3,4], 2))

print(sliding_window_max([5], 1))
