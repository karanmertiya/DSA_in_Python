# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain two pointers `odd` and `even`. Keep the `evenHead`. Loop to link `odd->next = even->next` and `even->next = odd->next`. Finally, link `odd->next = evenHead`.

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head
    odd, even, evenHead = head, head.next, head.next
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = evenHead
    return head

