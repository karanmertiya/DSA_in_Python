# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use a dummy node. Iteratively swap `curr` and `curr->next`. Keep track of `prev` to link the swapped pairs to the rest of the list.

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

