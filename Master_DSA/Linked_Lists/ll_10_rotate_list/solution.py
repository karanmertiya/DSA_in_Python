# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Compute the length of the list, and make it a circular list by connecting the last node to head. Then find the new break point `(length - k % length)`. Break the circle and return the new head.

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0: return head
    length = 1
    cur = head
    while cur.next:
        length += 1
        cur = cur.next
    cur.next = head
    k = k % length
    k = length - k
    for _ in range(k): cur = cur.next
    head = cur.next
    cur.next = None
    return head

