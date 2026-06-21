# Time Complexity: O(max(N, M))
# Space Complexity: O(max(N, M))
# Explanation: Reverse both linked lists. Traverse both lists simultaneously, adding the data values of corresponding nodes along with the carry. Create new nodes for the sum and append them to the result list. Finally, reverse the result list.

def addTwoLists(first, second):
    def reverse(node):
        curr, prev, nxt = node, None, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    first = reverse(first)
    second = reverse(second)
    dummy = Node(0)
    temp = dummy
    carry = 0
    while first or second or carry:
        total = carry
        if first: total += first.data; first = first.next
        if second: total += second.data; second = second.next
        carry = total // 10
        temp.next = Node(total % 10)
        temp = temp.next
    return reverse(dummy.next)

