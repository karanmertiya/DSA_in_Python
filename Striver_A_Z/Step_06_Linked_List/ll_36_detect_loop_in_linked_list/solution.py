# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use Floyd's Cycle Detection algorithm (Tortoise and Hare). Move `slow` by 1 and `fast` by 2. If they meet, a loop exists. If `fast` reaches NULL, there is no loop.

def detectLoop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

