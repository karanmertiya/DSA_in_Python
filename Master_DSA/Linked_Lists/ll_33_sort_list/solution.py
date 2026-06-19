# Time Complexity: O(N log N)
# Space Complexity: O(log N) due to recursion stack
# Explanation: Merge sort for linked lists. Find mid using fast and slow pointers, split list into two, recursively sort, and merge the two sorted halves.

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(mid)
    dummy = ListNode(0)
    tail = dummy
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    if left: tail.next = left
    if right: tail.next = right
    return dummy.next

