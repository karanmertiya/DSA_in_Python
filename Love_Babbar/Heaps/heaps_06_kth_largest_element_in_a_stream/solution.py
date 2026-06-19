# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Maintain a Min Heap of size K. As elements arrive, add them to the heap if the heap has less than K elements. If the heap has K elements and the new element is greater than the top, pop the top and insert the new element. Print the top if heap size is K, else -1.

import heapq
def kthLargest(k, arr, n):
    pq = []
    ans = []
    for num in arr:
        if len(pq) < k: heapq.heappush(pq, num)
        elif num > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, num)
        if len(pq) < k: ans.append(-1)
        else: ans.append(pq[0])
    return ans

