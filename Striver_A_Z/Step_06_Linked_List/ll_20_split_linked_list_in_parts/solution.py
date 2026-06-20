# Time Complexity: O(N)
# Space Complexity: O(K)
# Explanation: First, calculate the length of the list. Then, determine base size `len / k` and extra nodes `len % k`. Iterate through the list, breaking it into parts of appropriate sizes.

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    length = 0
    curr = head
    while curr:
        length += 1
        curr = curr.next
    partSize, extra = length // k, length % k
    ans = []
    curr = head
    for i in range(k):
        ans.append(curr)
        currentPartSize = partSize + (1 if extra > 0 else 0)
        extra -= 1
        for _ in range(currentPartSize - 1):
            if curr: curr = curr.next
        if curr:
            nextPart = curr.next
            curr.next = None
            curr = nextPart
    return ans

