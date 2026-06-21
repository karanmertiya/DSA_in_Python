# Time Complexity: O(N * K * log K)
# Space Complexity: O(K)
# Explanation: Create a min-heap and push the head of each linked list into it. Pop the minimum element, append it to the result list, and if the popped node has a next node, push the next node into the heap. Continue until the heap is empty.

import heapq
def mergeKLists(arr: List[Node], K: int) -> Node:
    pq = []
    for i in range(K):
        if arr[i]:
            heapq.heappush(pq, (arr[i].data, i, arr[i]))
    dummy = Node(0)
    tail = dummy
    while pq:
        val, idx, curr = heapq.heappop(pq)
        tail.next = curr
        tail = tail.next
        if curr.next:
            heapq.heappush(pq, (curr.next.data, idx, curr.next))
    return dummy.next

