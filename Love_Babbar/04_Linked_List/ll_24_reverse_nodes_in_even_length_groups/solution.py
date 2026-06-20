# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse the list while tracking the expected group length. First, count the actual number of nodes left in the current group. If the count is even, reverse this sublist and connect it to the previous part. If odd, just skip. Update lengths and pointers.

def reverseEvenLengthGroups(head: Optional[ListNode]) -> Optional[ListNode]:
    groupLen = 1
    prev, curr = None, head
    while curr:
        temp, count = curr, 0
        while count < groupLen and temp:
            temp = temp.next
            count += 1
        if count % 2 == 0:
            gPrev, gCurr = None, curr
            for _ in range(count):
                nxt = gCurr.next
                gCurr.next = gPrev
                gPrev = gCurr
                gCurr = nxt
            prev.next = gPrev
            curr.next = gCurr
            prev = curr
            curr = gCurr
        else:
            for _ in range(count):
                prev = curr
                curr = curr.next
        groupLen += 1
    return head

