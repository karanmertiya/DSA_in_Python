# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use two pointers, `fast` and `slow`. Move `fast` `N` steps ahead. If `fast` becomes NULL before `N` steps, return -1 (N > length). Then move both `fast` and `slow` one step at a time until `fast` reaches the end. `slow` will be pointing to the Nth node from the end.

def getNthFromLast(head: Node, n: int) -> int:
    fast, slow = head, head
    for _ in range(n):
        if not fast: return -1
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.data

