# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: Use a dummy head for the sorted part. For each node in the original list, iterate through the sorted part to find its correct position and insert it.

def insertionSortList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = head
    while curr:
        prev = dummy
        while prev.next and prev.next.val <= curr.val:
            prev = prev.next
        nxt = curr.next
        curr.next = prev.next
        prev.next = curr
        curr = nxt
    return dummy.next

