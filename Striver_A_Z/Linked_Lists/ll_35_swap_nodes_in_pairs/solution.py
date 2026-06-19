# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a dummy node. Maintain a `prev` pointer. While `prev->next` and `prev->next->next` exist, swap them and move `prev` two steps ahead.

def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next

