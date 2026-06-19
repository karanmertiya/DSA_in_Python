# Time Complexity: O(K^2 log K)
# Space Complexity: O(K)
# Explanation: Use a Min Heap to store the first element of each array along with its 2D index. Extract the minimum element, add it to the result, and insert the next element from the same array into the Min Heap.

import heapq
def mergeKArrays(arr, K):
    pq = []
    for i in range(K): heapq.heappush(pq, (arr[i][0], i, 0))
    ans = []
    while pq:
        val, i, j = heapq.heappop(pq)
        ans.append(val)
        if j + 1 < K: heapq.heappush(pq, (arr[i][j + 1], i, j + 1))
    return ans

