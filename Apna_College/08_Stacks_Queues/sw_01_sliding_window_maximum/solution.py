# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Use a deque to store indices. The deque maintains elements in decreasing order. Remove elements from the back if they are smaller than the current element. Remove elements from the front if they are out of the window. The front element is the maximum of the current window.

import collections
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    res = []
    dq = collections.deque()
    for i in range(len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

