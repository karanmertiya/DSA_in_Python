# Time Complexity: O(K log N)
# Space Complexity: O(N)
# Explanation: Similar to merging K sorted arrays. Push the first element of each row into a min-heap. Pop the minimum element `K-1` times, pushing the next element from the popped element's row. The Kth popped element is the answer. (Binary Search is also optimal here).

import heapq
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    pq = []
    for i in range(n):
        heapq.heappush(pq, (matrix[i][0], i, 0))
    for _ in range(k - 1):
        val, r, c = heapq.heappop(pq)
        if c + 1 < n:
            heapq.heappush(pq, (matrix[r][c + 1], r, c + 1))
    return pq[0][0]

