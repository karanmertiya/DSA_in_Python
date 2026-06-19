# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Maintain a min-heap of size K. For each element in the stream, push it to the heap. If the heap size exceeds K, pop the top (minimum) element. The top of the heap is the Kth largest element. If the size is less than K, return -1.

import heapq
def kthLargest(k: int, arr: List[int], n: int) -> List[int]:
    pq = []
    res = []
    for i in range(n):
        heapq.heappush(pq, arr[i])
        if len(pq) > k:
            heapq.heappop(pq)
        if len(pq) < k:
            res.append(-1)
        else:
            res.append(pq[0])
    return res

