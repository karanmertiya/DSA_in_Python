# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterate through the list. When a node has a child, find the tail of the child list. Connect the tail to `node->next`, and `node->next` to the child. Update `prev` pointers. Set `node->child` to `nullptr`.

def flatten(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: return None
    curr = head
    while curr:
        if curr.child:
            tail = curr.child
            while tail.next: tail = tail.next
            tail.next = curr.next
            if curr.next: curr.next.prev = tail
            curr.next = curr.child
            curr.child.prev = curr
            curr.child = None
        curr = curr.next
    return head

