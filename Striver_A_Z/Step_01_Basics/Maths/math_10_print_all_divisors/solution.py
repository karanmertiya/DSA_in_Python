# Time Complexity: O(sqrt(N) + k log k)
# Space Complexity: O(k)
# Explanation: Iterate `i` from 1 to `sqrt(N)`. If `N % i == 0`, add `i` to the list of divisors. If `N / i != i`, also add `N / i`. Sort the list before returning.

def print_divisors(n):
    ans = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ans.append(i)
            if n // i != i: ans.append(n // i)
    ans.sort()
    print(*(ans))

