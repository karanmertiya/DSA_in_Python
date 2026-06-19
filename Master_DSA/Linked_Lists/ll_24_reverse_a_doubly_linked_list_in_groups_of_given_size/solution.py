# Time Complexity: O(N)
# Space Complexity: O(N/K) recursion stack
# Explanation: Similar to reversing singly linked list in groups of k. Keep track of prev, next, and current. Reverse k nodes, then recursively call for the rest of the list.

def revListInGroupOfGivenSize(head, k):
    if not head: return None
    current = head
    next_node = None
    new_head = None
    count = 0
    while current and count < k:
        next_node = current.next
        current.prev = next_node
        current.next = new_head
        if new_head:
            new_head.prev = current
        new_head = current
        current = next_node
        count += 1
    if next_node:
        head.next = revListInGroupOfGivenSize(next_node, k)
        head.next.prev = head
    return new_head

