# Time Complexity: O(max(N, M))
# Space Complexity: O(max(N, M))
# Explanation: Iterate through both lists, keeping a `carry`. Create new nodes for the `sum % 10`.

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = temp = ListNode()
    carry = 0
    while l1 or l2 or carry:
        s = carry
        if l1: s += l1.val; l1 = l1.next
        if l2: s += l2.val; l2 = l2.next
        carry = s // 10
        temp.next = ListNode(s % 10)
        temp = temp.next
    return dummy.next

