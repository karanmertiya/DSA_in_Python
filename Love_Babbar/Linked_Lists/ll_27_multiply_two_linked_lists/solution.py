# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Traverse both linked lists to form the respective numbers modulo a given large number (e.g., 10^9+7). Then multiply the two formed numbers and return the result modulo the same large number.

def multiplyTwoLists(head1, head2):
    MOD = 1000000007
    num1, num2 = 0, 0
    while head1:
        num1 = (num1 * 10 + head1.data) % MOD
        head1 = head1.next
    while head2:
        num2 = (num2 * 10 + head2.data) % MOD
        head2 = head2.next
    return (num1 * num2) % MOD

