# Time Complexity: O(N log K)
# Space Complexity: O(K)
# Explanation: Push the head of each list into a min-heap. Extract the minimum node, append it to the merged list, and push its next node (if any) into the min-heap. Repeat until heap is empty.

import heapq
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    setattr(ListNode, "__lt__", lambda self, other: self.val < other.val)
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)
    dummy = tail = ListNode(0)
    while heap:
        curr = heapq.heappop(heap)
        tail.next = curr
        tail = tail.next
        if curr.next:
            heapq.heappush(heap, curr.next)
    return dummy.next

