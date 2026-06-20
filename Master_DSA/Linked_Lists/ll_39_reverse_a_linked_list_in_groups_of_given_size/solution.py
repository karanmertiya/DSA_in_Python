# Time Complexity: O(N)
# Space Complexity: O(N/K)
# Explanation: Reverse the first `k` nodes of the linked list iteratively. After reversing, the `head` pointer will be the end of the reversed group, and `curr` will point to the next node. Recursively call the function for `curr` and set `head->next` to the result.

def reverse(head: Node, k: int) -> Node:
    if not head: return None
    curr, prev, nxt = head, None, None
    count = 0
    while curr and count < k:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        count += 1
    if nxt:
        head.next = reverse(nxt, k)
    return prev

