# Time Complexity: O(N) (Constraint)
# Space Complexity: O(1) (Constraint)
# Explanation: Iterative approach: Maintain three pointers (`prev`, `curr`, `next_node`). Re-point `curr->next` to `prev` and slide forward.

def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

