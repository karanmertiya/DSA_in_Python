# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Use a double-ended queue (deque) to store indices. Maintain indices in the deque such that the elements they correspond to are in decreasing order. The front of the deque will always be the maximum for the current window. Remove indices from the front if they are out of the window (`i - k`).

from collections import deque
def maxSlidingWindow(nums, k):
    dq = deque()
    ans = []
    for i in range(len(nums)):
        if dq and dq[0] == i - k: dq.popleft()
        while dq and nums[dq[-1]] < nums[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: ans.append(nums[dq[0]])
    return ans

