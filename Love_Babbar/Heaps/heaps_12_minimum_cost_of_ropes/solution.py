# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Explanation: Use a Min Heap to always pick the two smallest ropes. Add their sum to the total cost and insert the merged rope back into the heap. Repeat until one rope is left.

import heapq
def minCost(arr, n):
    heapq.heapify(arr)
    cost = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        cost += (a + b)
        heapq.heappush(arr, a + b)
    return cost

