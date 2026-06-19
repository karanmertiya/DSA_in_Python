# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Create a Min Heap of size k+1. Insert the first k+1 elements into the heap. Then, pop the minimum element, place it in the sorted list, and push the next element from the original list into the heap.

import heapq
def sortAKSortedDLL(head, k):
    if not head: return head
    pq = []
    newHead, last = None, None
    i = 0
    while head and i <= k:
        heapq.heappush(pq, (head.data, id(head), head))
        head = head.next
        i += 1
    while pq:
        _, _, minNode = heapq.heappop(pq)
        if not newHead:
            newHead = minNode
            newHead.prev = None
            last = newHead
        else:
            last.next = minNode
            minNode.prev = last
            last = minNode
        if head:
            heapq.heappush(pq, (head.data, id(head), head))
            head = head.next
    last.next = None
    return newHead

