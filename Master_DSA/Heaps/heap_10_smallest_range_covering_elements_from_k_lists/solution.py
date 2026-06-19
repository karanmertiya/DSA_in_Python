# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Use a min-heap storing `(value, list_idx, elem_idx)`. Also maintain the `current_max` of the elements currently in the heap. The current range is `[heap_top, current_max]`. Pop the min, push the next element from its list, and update `current_max`. Continue until any list is exhausted.

import heapq
def smallestRange(nums: List[List[int]]) -> List[int]:
    pq = []
    currMax = float('-inf')
    for i in range(len(nums)):
        heapq.heappush(pq, (nums[i][0], i, 0))
        currMax = max(currMax, nums[i][0])
    ans = [pq[0][0], currMax]
    while True:
        val, r, c = heapq.heappop(pq)
        if currMax - val < ans[1] - ans[0]:
            ans = [val, currMax]
        if c + 1 == len(nums[r]):
            break
        next_val = nums[r][c + 1]
        heapq.heappush(pq, (next_val, r, c + 1))
        currMax = max(currMax, next_val)
    return ans

