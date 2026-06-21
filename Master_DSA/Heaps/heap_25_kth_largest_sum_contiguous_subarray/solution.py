# Time Complexity: O(N^2 log K)
# Space Complexity: O(N + K)
# Explanation: Iterate through all possible subarrays and calculate their sums using a prefix sum array. Maintain a Min Heap of size K to keep track of the top K sums. At the end, the top of the Min Heap is the K-th largest sum.

import heapq
def kthLargestSum(arr, n, k):
    sum_arr = [0] * (n + 1)
    for i in range(1, n + 1): sum_arr[i] = sum_arr[i - 1] + arr[i - 1]
    pq = []
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            x = sum_arr[j] - sum_arr[i - 1]
            if len(pq) < k: heapq.heappush(pq, x)
            elif x > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, x)
    return pq[0]

