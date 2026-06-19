# Time Complexity: O(N)
# Space Complexity: O(N/k) recursive stack
# Explanation: Reverse the first k nodes iteratively. The next node becomes the head of the remaining list. Recursively call the function for the rest of the list and attach it to the tail of the reversed group (which is `head`). Return the new head.

def reverse(head, k):
    if not head: return None
    curr, prev, next_node = head, None, None
    count = 0
    while curr and count < k:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        count += 1
    if next_node: head.next = reverse(next_node, k)
    return prev

