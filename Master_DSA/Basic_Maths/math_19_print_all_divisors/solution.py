# Time Complexity: O(sqrt(N) + k log k)
# Space Complexity: O(k)
# Explanation: Iterate up to sqrt(N). If 'i' divides N, then 'N/i' is also a divisor. Iterating up to N (O(N) time) is unnecessary and inefficient.

def print_divisors(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i != i: ans.append(n // i)
    ans.sort()
    print(*(ans))

