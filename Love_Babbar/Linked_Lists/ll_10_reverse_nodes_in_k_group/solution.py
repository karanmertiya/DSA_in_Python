# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterative approach. Calculate the length. Use a dummy node. Maintain `pre`, `curr`, and `nex` pointers. Reverse `k-1` links in each group. Decrement length by `k` until length < `k`.

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k == 1: return head
    length, temp = 0, head
    while temp:
        length += 1
        temp = temp.next
    dummy = ListNode(0)
    dummy.next = head
    pre, curr, nex = dummy, dummy, dummy
    while length >= k:
        curr = pre.next
        nex = curr.next
        for _ in range(1, k):
            curr.next = nex.next
            nex.next = pre.next
            pre.next = nex
            nex = curr.next
        pre = curr
        length -= k
    return dummy.next

