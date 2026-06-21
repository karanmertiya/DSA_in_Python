# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Two pointers `a` and `b`. Traverse `A` then `B`, and `B` then `A`. They will meet at the intersection node or `NULL`.

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

