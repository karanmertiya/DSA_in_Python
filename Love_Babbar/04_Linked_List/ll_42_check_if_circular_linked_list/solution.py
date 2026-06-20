# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse the linked list starting from head. If we reach NULL, it's not circular. If we reach head again, it is circular.

def isCircular(head):
    if head is None: return True
    temp = head.next
    while temp is not None and temp != head:
        temp = temp.next
    return temp == head

