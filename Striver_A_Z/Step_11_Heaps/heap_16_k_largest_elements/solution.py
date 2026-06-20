# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Maintain a min-heap of size K. Iterate through the array. If the heap has < K elements, push. Else if the current element > heap's top, pop the top and push the current element. The heap will contain the K largest elements.

import heapq
def kLargest(arr: List[int], n: int, k: int) -> List[int]:
    pq = []
    for i in range(n):
        heapq.heappush(pq, arr[i])
        if len(pq) > k:
            heapq.heappop(pq)
    return sorted(pq, reverse=True)

