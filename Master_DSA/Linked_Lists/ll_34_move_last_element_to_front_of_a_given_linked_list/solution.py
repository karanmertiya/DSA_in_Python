# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse the list to find the last node (`tail`) and the second last node (`sec_last`). Make `sec_last->next = NULL`, `tail->next = head`, and update `head = tail`.

def moveToFront(head):
    if not head or not head.next: return head
    sec_last = None
    tail = head
    while tail.next:
        sec_last = tail
        tail = tail.next
    sec_last.next = None
    tail.next = head
    return tail

