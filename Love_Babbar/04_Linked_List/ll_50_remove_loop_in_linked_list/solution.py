# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use Floyd's Cycle Detection. If a loop is found, reset `slow` to head. Move both `slow` and `fast` by 1. The node where they meet is the start of the loop. Keep track of `fast`'s previous node to set its `next` to NULL.

def removeLoop(head):
    if not head or not head.next: return
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break
    if slow == fast:
        slow = head
        if slow == fast:
            while fast.next != slow: fast = fast.next
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        fast.next = None

