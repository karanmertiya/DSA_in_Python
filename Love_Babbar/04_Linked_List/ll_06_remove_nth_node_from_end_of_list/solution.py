# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Two-pointer approach. Move `fast` pointer `n` steps ahead. Then move both `slow` and `fast` until `fast` reaches the end. `slow` will be right before the target node.

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast: return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

