# Time Complexity: O(log(min(A, B)))
# Space Complexity: O(1)
# Explanation: Use Euclidean algorithm. `gcd(A, B) = gcd(B, A % B)`. Repeat until `B` becomes 0, then `A` is the GCD.

def gcd(A, B):
    while A > 0 and B > 0:
        if A > B: A %= B
        else: B %= A
    return B if A == 0 else A

