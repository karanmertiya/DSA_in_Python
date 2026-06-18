# Time Complexity: O(N) (Trade-off)
# Space Complexity: O(1)
# Explanation: Iterate from 1 to N sequentially, checking for divisibility.

def print_divisors_brute(n: int) -> None:
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

# Time Complexity: O(&radic;N * log(&radic;N)) (Constraint)
# Space Complexity: O(&radic;N) (Trade-off)
# Explanation: Iterate up to sqrt(N) to find pairs of divisors, then sort ascending.

def print_divisors_optimal(n: int) -> None:
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            # Edge Case: Avoid duplicate addition for perfect square roots
            if n // i != i:
                divisors.append(n // i)
    divisors.sort()
    for d in divisors:
        print(d, end=" ")

