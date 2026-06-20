# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Use a deque to store indices of elements. The deque will maintain elements in decreasing order. For each element, remove elements from the back of the deque that are smaller than the current element. Also, remove elements from the front that are out of the current window. The front of the deque will always have the maximum element of the current window.

import collections
def max_of_subarrays(arr: List[int], n: int, k: int) -> List[int]:
    res = []
    dq = collections.deque()
    for i in range(n):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(arr[dq[0]])
    return res

