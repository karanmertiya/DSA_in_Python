# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Reverse the linked list. Keep track of the max node seen so far. If a node is less than the max node, delete it. Else, update max node. Finally, reverse the list back.

def reverse(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

def compute(head):
    head = reverse(head)
    curr = head
    maxNode = head
    while curr and curr.next:
        if curr.next.data < maxNode.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
            maxNode = curr
    return reverse(head)

