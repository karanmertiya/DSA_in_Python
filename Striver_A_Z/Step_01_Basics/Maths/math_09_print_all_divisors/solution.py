# Time Complexity: O(N)
# Space Complexity: O(1)
# Explanation: Brute Force: Iterate from 1 to N and check if N % i == 0.

def printDivisors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

# Time Complexity: O(sqrt(N) + k log k)
# Space Complexity: O(k)
# Explanation: Optimal: Iterate up to sqrt(N). If 'i' divides N, then 'N/i' is also a divisor.

def print_divisors(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i != i: ans.append(n // i)
    ans.sort()
    print(*(ans))

