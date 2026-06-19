# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse the DLL. For each node, swap its `prev` and `next` pointers. The new head will be the last node processed.

def reverseDLL(head):
    if not head or not head.next: return head
    curr = head
    temp = None
    while curr:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
    return temp.prev

