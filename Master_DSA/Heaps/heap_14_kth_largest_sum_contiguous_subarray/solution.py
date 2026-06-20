# Time Complexity: O(N^2 log K)
# Space Complexity: O(K)
# Explanation: Iterate all subarrays using two nested loops. Maintain a min-heap of size K to store the top K sums. If the heap size < K, push the current sum. If the heap size == K and current sum > heap top, pop and push current sum. The top of the heap is the Kth largest sum.

import heapq
def kthLargest(Arr: List[int], N: int, K: int) -> int:
    pq = []
    for i in range(N):
        s = 0
        for j in range(i, N):
            s += Arr[j]
            if len(pq) < K:
                heapq.heappush(pq, s)
            elif s > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, s)
    return pq[0]

