# Time Complexity: O(N log K) (Constraint)
# Space Complexity: O(K) (Constraint)
# Explanation: Use a Min-Heap of size K. When the heap exceeds size K, pop the minimum element. The top of the heap will be the Kth largest.

import heapq
def find_kth_largest(nums: list[int], k: int) -> int:
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

