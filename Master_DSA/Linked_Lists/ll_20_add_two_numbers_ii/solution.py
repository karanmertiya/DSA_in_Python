# Time Complexity: O(N + M)
# Space Complexity: O(N + M)
# Explanation: Use two stacks to store the digits of the lists. Pop from stacks, add along with carry, and construct the new list by inserting at the head.

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    s1, s2 = [], []
    while l1:
        s1.append(l1.val)
        l1 = l1.next
    while l2:
        s2.append(l2.val)
        l2 = l2.next
    carry = 0
    head = None
    while s1 or s2 or carry:
        sum_val = carry
        if s1: sum_val += s1.pop()
        if s2: sum_val += s2.pop()
        node = ListNode(sum_val % 10)
        node.next = head
        head = node
        carry = sum_val // 10
    return head

