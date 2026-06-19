# Time Complexity: O(N)
# Space Complexity: O(N)
# Explanation: Use a hash set to store the seen values. Iterate the list. If a node's value is in the set, skip it by updating the `next` pointer of the `prev` node. Else, add it to the set and update `prev`.

def removeDuplicates(head):
    if not head: return None
    seen = set()
    curr, prev = head, None
    while curr:
        if curr.data in seen:
            prev.next = curr.next
            curr = prev.next
        else:
            seen.add(curr.data)
            prev = curr
            curr = curr.next
    return head

