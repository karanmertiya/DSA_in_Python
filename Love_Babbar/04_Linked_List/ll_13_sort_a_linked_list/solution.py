# Time Complexity: O(N log N)
# Space Complexity: O(log N)
# Explanation: Merge Sort. Use fast/slow pointers to find the middle of the linked list. Split into two halves, recursively sort both halves, then merge the two sorted halves.

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    def mergeTwoLists(list1, list2):
        dummy = ListNode(0)
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1; list1 = list1.next
            else:
                tail.next = list2; list2 = list2.next
            tail = tail.next
        tail.next = list1 if list1 else list2
        return dummy.next
    if not head or not head.next: return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next; fast = fast.next.next
    mid = slow.next
    slow.next = None
    return mergeTwoLists(sortList(head), sortList(mid))

