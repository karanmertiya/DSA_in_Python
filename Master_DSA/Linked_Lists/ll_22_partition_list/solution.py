# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Maintain two separate linked lists: `before` and `after` with their own dummy heads. Iterate through original list, appending to `before` or `after` based on value. Then link `before` tail to `after` head.

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    before_head = ListNode(0)
    before = before_head
    after_head = ListNode(0)
    after = after_head
    while head:
        if head.val < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next
    after.next = None
    before.next = after_head.next
    return before_head.next

