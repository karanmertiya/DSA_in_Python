# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Use a Min-Heap. Push the head of each linked list into the Priority Queue. Continuously pop the smallest, append it to result, and push its `next` node into the PQ.

import heapq
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    pq = []
    for i, l in enumerate(lists):
        if l: heapq.heappush(pq, (l.val, i, l))
    dummy = ListNode(0)
    tail = dummy
    while pq:
        val, i, node = heapq.heappop(pq)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(pq, (node.next.val, i, node.next))
    return dummy.next

