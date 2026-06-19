# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse to the Nth node. This will be the new tail. Its next will be the new head. Traverse to the end of the list and link it to the original head.

def rotateDLL(start, N):
    if N == 0: return start
    current = start
    count = 1
    while count < N and current:
        current = current.next
        count += 1
    if not current: return start
    nthNode = current
    while current.next:
        current = current.next
    current.next = start
    start.prev = current
    start = nthNode.next
    start.prev = None
    nthNode.next = None
    return start

