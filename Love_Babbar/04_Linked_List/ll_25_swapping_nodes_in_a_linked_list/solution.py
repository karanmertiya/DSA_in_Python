# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two pointers. Move `fast` pointer `k-1` steps. `first_node` is at `fast`. Initialize `slow = head`. Move both `slow` and `fast` to the end. `slow` will be at `second_node`. Swap values.

def swapNodes(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    fast = head
    for _ in range(k - 1): fast = fast.next
    first_node = fast
    slow = head
    while fast.next:
        slow = slow.next
        fast = fast.next
    first_node.val, slow.val = slow.val, first_node.val
    return head

