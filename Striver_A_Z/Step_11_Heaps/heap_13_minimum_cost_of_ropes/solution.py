# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use a min-heap. Pop two minimum length ropes, add them up, add sum to total cost, and push the merged rope back to the heap. Repeat until one rope remains.

import heapq
def minCost(arr: List[int], n: int) -> int:
    pq = list(arr)
    heapq.heapify(pq)
    cost = 0
    while len(pq) > 1:
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        cost += a + b
        heapq.heappush(pq, a + b)
    return cost

