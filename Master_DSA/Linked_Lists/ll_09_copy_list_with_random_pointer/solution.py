# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: 3 Steps O(1) space. 1) Insert copy nodes right after original nodes. 2) Set random pointers for copy nodes: `iter->next->random = iter->random ? iter->random->next : NULL`. 3) Separate the two lists.

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: return None
    iter_node = head
    while iter_node:
        copy = Node(iter_node.val)
        copy.next = iter_node.next
        iter_node.next = copy
        iter_node = copy.next
    iter_node = head
    while iter_node:
        if iter_node.random: iter_node.next.random = iter_node.random.next
        iter_node = iter_node.next.next
    iter_node = head
    pseudoHead = Node(0)
    copyIter = pseudoHead
    while iter_node:
        nextIter = iter_node.next.next
        copyIter.next = iter_node.next
        iter_node.next = nextIter
        copyIter = copyIter.next
        iter_node = nextIter
    return pseudoHead.next

