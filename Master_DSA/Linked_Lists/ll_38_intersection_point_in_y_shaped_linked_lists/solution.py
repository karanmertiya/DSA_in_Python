# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Use two pointers `a` and `b`. Traverse both lists. When `a` reaches the end, redirect it to `head2`. When `b` reaches the end, redirect it to `head1`. They will meet at the intersection point or both become NULL.

def intersectPoint(head1, head2):
    a, b = head1, head2
    while a != b:
        a = a.next if a else head2
        b = b.next if b else head1
    if a: return a.data
    return -1

