# Time Complexity: O(N + M)
# Space Complexity: O(1)
# Explanation: Traverse the first linked list and compute the number it represents modulo 10^9+7. Do the same for the second linked list. Multiply the two numbers and return the result modulo 10^9+7.

def multiplyTwoLists(head1: Node, head2: Node) -> int:
    num1 = num2 = 0
    mod = 10**9 + 7
    while head1:
        num1 = (num1 * 10 + head1.data) % mod
        head1 = head1.next
    while head2:
        num2 = (num2 * 10 + head2.data) % mod
        head2 = head2.next
    return (num1 * num2) % mod

