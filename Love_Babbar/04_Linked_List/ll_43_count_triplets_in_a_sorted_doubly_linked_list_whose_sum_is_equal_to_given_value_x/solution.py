# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Explanation: Iterate through the list. For each node, use two pointers (left and right) on the remaining list to find pairs that sum to `x - node.data`.

def countTriplets(head, x):
    if head is None: return 0
    last = head
    while last.next: last = last.next
    count = 0
    curr = head
    while curr:
        first = curr.next
        right = last
        while first and right and first != right and right.next != first:
            total = curr.data + first.data + right.data
            if total == x:
                count += 1
                first = first.next
                right = right.prev
            elif total < x:
                first = first.next
            else:
                right = right.prev
        curr = curr.next
    return count

