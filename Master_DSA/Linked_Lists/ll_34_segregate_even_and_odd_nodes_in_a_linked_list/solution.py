# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Create two dummy nodes, one for the even list and one for the odd list. Traverse the original list and append even nodes to the even list and odd nodes to the odd list. Finally, connect the end of the even list to the head of the odd list and terminate the odd list with NULL.

def divide(N: int, head: Node) -> Node:
    evenStart = evenEnd = None
    oddStart = oddEnd = None
    curr = head
    while curr:
        val = curr.data
        if val % 2 == 0:
            if not evenStart:
                evenStart = evenEnd = curr
            else:
                evenEnd.next = curr
                evenEnd = evenEnd.next
        else:
            if not oddStart:
                oddStart = oddEnd = curr
            else:
                oddEnd.next = curr
                oddEnd = oddEnd.next
        curr = curr.next
    if not oddStart or not evenStart: return head
    evenEnd.next = oddStart
    oddEnd.next = None
    return evenStart

