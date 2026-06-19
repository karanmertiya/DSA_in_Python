# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Compute length `N` of list. Connect tail to head to form a cycle. Find `k = k % N`. Move `N - k` steps from head. The new head is `current->next`. Break the cycle by setting `current->next = NULL`.

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0: return head
    cur = head
    length = 1
    while cur.next:
        length += 1
        cur = cur.next
    cur.next = head
    k = k % length
    k = length - k
    while k > 0:
        cur = cur.next
        k -= 1
    head = cur.next
    cur.next = None
    return head

