# Time Complexity: O(N * K * log K)
# Space Complexity: O(K)
# Explanation: Maintain a min-heap of size K, storing the first element of each list along with its list index and element index. Keep track of the `max_val` currently in the heap. The current range is `[heap_min, max_val]`. Extract the min, update the smallest range if needed, and insert the next element from the extracted element's list. Update `max_val` with the new element.

import heapq
def findSmallestRange(KSortedArray: List[List[int]], n: int, k: int) -> List[int]:
    pq = []
    mx = float('-inf')
    for i in range(k):
        heapq.heappush(pq, (KSortedArray[i][0], i, 0))
        mx = max(mx, KSortedArray[i][0])
    ans_range = float('inf')
    start, end = -1, -1
    while pq:
        mn, row, col = heapq.heappop(pq)
        if mx - mn < ans_range:
            ans_range = mx - mn
            start, end = mn, mx
        if col + 1 < n:
            next_val = KSortedArray[row][col+1]
            heapq.heappush(pq, (next_val, row, col+1))
            mx = max(mx, next_val)
        else:
            break
    return [start, end]

