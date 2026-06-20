# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Reverse the linked list. Traverse the reversed list and keep track of the maximum value seen so far. If a node's value is less than the maximum, delete it. Otherwise, update the maximum. Finally, reverse the list again.

def compute(head: Node) -> Node:
    def reverseList(node):
        prev, curr = None, node
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    head = reverseList(head)
    curr = head
    max_val = head.data
    while curr and curr.next:
        if curr.next.data < max_val:
            curr.next = curr.next.next
        else:
            curr = curr.next
            max_val = curr.data
    return reverseList(head)

