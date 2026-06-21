# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Use slow and fast pointers to find the mid of the circular linked list. The slow pointer will point to the mid. Then break the list into two and make both circular.

def splitList(head, head1, head2):
    if head is None: return
    slow, fast = head, head
    while fast.next != head and fast.next.next != head:
        slow = slow.next
        fast = fast.next.next
    if fast.next.next == head:
        fast = fast.next
    head1.head = head
    if head.next != head:
        head2.head = slow.next
    fast.next = slow.next
    slow.next = head

