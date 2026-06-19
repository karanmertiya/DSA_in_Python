# Time Complexity: O(N * K log K)
# Space Complexity: O(K)
# Explanation: Similar to merging K sorted arrays, use a Min Heap storing `(value, list_idx, element_idx)`. Also maintain the `max_val` seen so far among the current elements. The range is `[min_heap_top, max_val]`. Update the range if the difference is smaller. Pop the min and push the next element from the same list, updating `max_val`.

import heapq
def findSmallestRange(KSortedArray, n, k):
    pq = []
    max_val = float('-inf')
    for i in range(k):
        heapq.heappush(pq, (KSortedArray[i][0], i, 0))
        max_val = max(max_val, KSortedArray[i][0])
    range_min, range_max, range_diff = 0, float('inf'), float('inf')
    while True:
        min_val, r, c = heapq.heappop(pq)
        if max_val - min_val < range_diff:
            range_diff = max_val - min_val
            range_min, range_max = min_val, max_val
        if c + 1 == n: break
        heapq.heappush(pq, (KSortedArray[r][c + 1], r, c + 1))
        max_val = max(max_val, KSortedArray[r][c + 1])
    return (range_min, range_max)

