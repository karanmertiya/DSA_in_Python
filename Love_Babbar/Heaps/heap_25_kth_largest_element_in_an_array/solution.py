# Time Complexity: O(N log K) Heap, O(N) avg Quickselect
# Space Complexity: O(K) Heap, O(1) Quickselect
# Explanation: Min-heap: Keep a min-heap of size K. The root is the Kth largest. Quickselect: Partition the array like in Quicksort, recursively searching only the partition containing the target index.

import heapq
def findKthLargest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]

