# Time Complexity: O(log2(N)) (Trade-off)
# Space Complexity: O(1)
# Explanation: Iteratively divide by 2. If it ever yields an odd number > 1, it is not a power of 2.

def is_power_of_two_brute(n: int) -> bool:
    if n <= 0: return False
    while n % 2 == 0:
        n //= 2
    return n == 1

# Time Complexity: O(1) (Constraint)
# Space Complexity: O(1)
# Explanation: A power of 2 has exactly 1 set bit. Thus `N & (N-1)` must equal 0.

def is_power_of_two_optimal(n: int) -> bool:
    return (n > 0) and ((n & (n - 1)) == 0)

