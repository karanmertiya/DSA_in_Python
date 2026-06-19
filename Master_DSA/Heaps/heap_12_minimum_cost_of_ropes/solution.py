# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Insert all lengths into a min-heap. While heap size > 1, extract the two minimum elements, add them, add their sum to the total cost, and insert their sum back into the heap.

import heapq
def minCost(arr: List[int], n: int) -> int:
    heapq.heapify(arr)
    cost = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        cost += (a + b)
        heapq.heappush(arr, a + b)
    return cost

