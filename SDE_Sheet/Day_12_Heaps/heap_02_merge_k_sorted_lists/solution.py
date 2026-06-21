# Time Complexity: O(N log K) (Constraint)
# Space Complexity: O(K) (Constraint)
# Explanation: Push the head of each list into a Min-Heap. Repeatedly pop the smallest node, attach it to the result list, and push its `next` node into the heap.

import heapq
def merge_k_lists(lists: list[ListNode]) -> ListNode:
    # To avoid comparing ListNodes directly in Python heapq, store (val, index, node)
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst.val, i, lst))
            
    dummy = ListNode(0)
    tail = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
            
    return dummy.next

