# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Iterate list. For each node, insert a copy node right after it. Then, iterate again and set `copy->random = original->random->next`. Finally, separate the original list and the copy list.

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: return None
    iter = head
    while iter:
        nxt = iter.next
        copy = Node(iter.val)
        iter.next = copy
        copy.next = nxt
        iter = nxt
    iter = head
    while iter:
        if iter.random:
            iter.next.random = iter.random.next
        iter = iter.next.next
    iter = head
    pseudoHead = Node(0)
    copy = pseudoHead
    while iter:
        nxt = iter.next.next
        copy.next = iter.next
        iter.next = nxt
        copy = copy.next
        iter = nxt
    return pseudoHead.next

