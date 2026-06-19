# Time Complexity: O(K log N) or O(N log(max-min))
# Space Complexity: O(N) or O(1)
# Explanation: Min-heap: Push the first element of each row. Pop `K-1` times, pushing the next element in the row of the popped element. The `K`th popped element is the answer. Binary search: search space `matrix[0][0]` to `matrix[n-1][n-1]`. Count elements <= `mid` using two pointers.

import heapq
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    n = len(matrix)
    pq = []
    for i in range(min(n, k)):
        heapq.heappush(pq, (matrix[i][0], i, 0))
    for _ in range(k - 1):
        val, r, c = heapq.heappop(pq)
        if c + 1 < n:
            heapq.heappush(pq, (matrix[r][c+1], r, c+1))
    return pq[0][0]

