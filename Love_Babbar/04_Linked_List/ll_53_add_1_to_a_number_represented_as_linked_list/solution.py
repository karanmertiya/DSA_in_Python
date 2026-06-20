# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Reverse the linked list. Add 1 to the first node, and propagate the carry if the value becomes 10. Once done, reverse the list back. If carry still remains at the end, add a new node.

def addOne(head):
    def reverse(node):
        curr, prev, nxt = node, None, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    head = reverse(head)
    curr, prev = head, None
    carry = 1
    while curr:
        total = curr.data + carry
        carry = total // 10
        curr.data = total % 10
        prev = curr
        curr = curr.next
    if carry > 0:
        prev.next = Node(carry)
    return reverse(head)

