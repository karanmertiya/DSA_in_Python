# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Count nodes. While `count >= k`, reverse `k` nodes. Keep track of previous group's tail to connect to current group's head. If `< k` nodes remain, just connect them.

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1: return head
    dummy = ListNode(0)
    dummy.next = head
    curr, nex, pre = dummy, dummy, dummy
    count = 0
    while curr.next:
        curr = curr.next
        count += 1
    while count >= k:
        curr = pre.next
        nex = curr.next
        for _ in range(1, k):
            curr.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = curr.next
        pre = curr
        count -= k
    return dummy.next

