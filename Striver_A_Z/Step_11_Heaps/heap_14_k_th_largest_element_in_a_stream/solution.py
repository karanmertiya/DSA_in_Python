# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Maintain a min-heap of size K. While processing the stream, if heap size is < K, push current element. If heap size == K and current element is > heap top, pop and push current element. Append heap top to result if size is K, else append -1.

import heapq
def kthLargest(k: int, arr: List[int], n: int) -> List[int]:
    res = []
    pq = []
    for i in range(n):
        if len(pq) < k:
            heapq.heappush(pq, arr[i])
        elif arr[i] > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, arr[i])
        if len(pq) < k:
            res.append(-1)
        else:
            res.append(pq[0])
    return res

