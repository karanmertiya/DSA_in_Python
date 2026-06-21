# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Use a Max Heap of size K. Iterate through the array. For the first K elements, insert them into the heap. For the remaining elements, if the element is smaller than the top of the heap, pop the top and insert the element. The top of the heap will be the Kth smallest element.

import heapq
def kthSmallest(arr, l, r, k):
    pq = []
    for i in range(l, r + 1):
        if len(pq) < k: heapq.heappush(pq, -arr[i])
        elif arr[i] < -pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, -arr[i])
    return -pq[0]

