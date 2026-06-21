# Time Complexity: O(N)
# Space Complexity: O(1) extra space if we modify in-place
# Explanation: Maintain a dummy node. Traverse the list. Maintain a running sum. When we encounter a 0 (and sum > 0), create a new node with `sum`, attach it to dummy list, reset `sum` to 0.

def mergeNodes(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = currDummy = ListNode(0)
    curr = head.next
    current_sum = 0
    while curr:
        if curr.val == 0:
            currDummy.next = ListNode(current_sum)
            currDummy = currDummy.next
            current_sum = 0
        else:
            current_sum += curr.val
        curr = curr.next
    return dummy.next

