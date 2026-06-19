# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use Floyd's cycle finding algorithm. Once `slow` and `fast` meet, move `slow` to the `head`. Then move both `slow` and `fast` by 1 step. They will meet at the starting node of the loop.

def findFirstNode(head):
    if not head: return -1
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break
    if slow != fast: return -1
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return slow.data

