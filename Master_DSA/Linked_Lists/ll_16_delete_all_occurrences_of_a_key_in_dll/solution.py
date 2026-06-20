# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse the list. If `node->data == x`, update the `next` pointer of `node->prev` and `prev` pointer of `node->next`. If the node is head, update head.

def deleteAllOccurOfX(head, x):
    curr = head
    while curr:
        if curr.data == x:
            if curr == head: head = curr.next
            if curr.prev: curr.prev.next = curr.next
            if curr.next: curr.next.prev = curr.prev
            curr = curr.next
        else:
            curr = curr.next
    return head

