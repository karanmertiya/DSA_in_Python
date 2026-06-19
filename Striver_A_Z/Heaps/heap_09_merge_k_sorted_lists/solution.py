# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Push the heads of all K lists into a Min-Heap. Pop the smallest node, append it to result, and if it has a next node, push the next node into the heap.

import heapq
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    pq = []
    for i, head in enumerate(lists):
        if head: heapq.heappush(pq, (head.val, i, head))
    while pq:
        val, i, node = heapq.heappop(pq)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(pq, (node.next.val, i, node.next))
    return dummy.next

