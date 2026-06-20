# Time Complexity: O(K^2 log K)
# Space Complexity: O(K)
# Explanation: Create a min-heap that stores a tuple: (value, array_index, element_index). Push the first element of each of the K arrays into the heap. While the heap is not empty, pop the minimum element, add it to the result, and if the array from which it was popped has more elements, push the next element to the heap.

import heapq
def mergeKArrays(arr: List[List[int]], K: int) -> List[int]:
    pq = []
    res = []
    for i in range(K):
        heapq.heappush(pq, (arr[i][0], i, 0))
    while pq:
        val, row, col = heapq.heappop(pq)
        res.append(val)
        if col + 1 < len(arr[row]):
            heapq.heappush(pq, (arr[row][col + 1], row, col + 1))
    return res

