# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Use a Min-Heap of size K. Push elements into the heap. If heap size exceeds K, pop the minimum element. The top of the heap at the end is the Kth largest element.

import heapq
def findKthLargest(nums: List[int], k: int) -> int:
    minH = []
    for num in nums:
        heapq.heappush(minH, num)
        if len(minH) > k:
            heapq.heappop(minH)
    return minH[0]

