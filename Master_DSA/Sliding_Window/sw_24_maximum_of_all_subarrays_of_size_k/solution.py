# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Same as LeetCode 239. Use a deque to maintain decreasing order of elements in the current window.

from collections import deque
def max_of_subarrays(arr, n, k):
    dq = deque()
    ans = []
    for i in range(n):
        if dq and dq[0] == i - k: dq.popleft()
        while dq and arr[dq[-1]] <= arr[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: ans.append(arr[dq[0]])
    return ans

