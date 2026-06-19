# Time Complexity: O(N + M)
# Space Complexity: O(N + M)
# Explanation: Use two pointers, `ptr1` for the first list and `ptr2` for the second. If `ptr1->data < ptr2->data`, `ptr1++`. If `ptr2->data < ptr1->data`, `ptr2++`. If they are equal, add to the result list and advance both.

def findIntersection(head1, head2):
    dummy = Node(0)
    temp = dummy
    p1, p2 = head1, head2
    while p1 and p2:
        if p1.data < p2.data: p1 = p1.next
        elif p2.data < p1.data: p2 = p2.next
        else:
            temp.next = Node(p1.data)
            temp = temp.next
            p1 = p1.next
            p2 = p2.next
    return dummy.next

