# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Find length of list. Traverse groups of size k. For each group, perform standard linked list reversal. Link the prev group's tail to the current reversed head.

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1: return head
    dummy = ListNode(0)
    dummy.next = head
    cur, pre, count = head, dummy, 0
    while cur: 
        count += 1; cur = cur.next
    while count >= k:
        cur = pre.next
        nex = cur.next
        for _ in range(1, k):
            cur.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = cur.next
        pre = cur
        count -= k
    return dummy.next

