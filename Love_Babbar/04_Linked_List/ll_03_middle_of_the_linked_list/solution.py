# Time Complexity: O(N/2) &cong; O(N) (Constraint)
# Space Complexity: O(1)
# Explanation: Use a slow pointer (moves 1 step) and a fast pointer (moves 2 steps). When fast reaches the end, slow is exactly at the middle.

def middle_node(head: ListNode) -> ListNode:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

