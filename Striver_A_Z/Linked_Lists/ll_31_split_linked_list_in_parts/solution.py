# Time Complexity: O(N)
# Space Complexity: O(k)
# Explanation: Count total nodes `N`. Each part will have at least `N // k` nodes, and the first `N % k` parts will have one extra node. Iterate and break the links.

def splitListToParts(head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
    ans = [None] * k
    n = 0
    node = head
    while node:
        n += 1
        node = node.next
    part, extra = divmod(n, k)
    node = head
    prev = None
    for i in range(k):
        if not node: break
        ans[i] = node
        for j in range(part + (1 if extra > 0 else 0)):
            prev = node
            node = node.next
        if prev: prev.next = None
        extra -= 1
    return ans

