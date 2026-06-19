# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: Monotonic Deque. Store indices in a double-ended queue. Maintain elements in strictly decreasing order. Pop front if it's out of window bounds. Add nums[dq.front()] to answer once window reaches size k.

from collections import deque
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    dq = deque()
    ans = []
    for i in range(len(nums)):
        if dq and dq[0] == i - k: dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]: dq.pop()
        dq.append(i)
        if i >= k - 1: ans.append(nums[dq[0]])
    return ans

