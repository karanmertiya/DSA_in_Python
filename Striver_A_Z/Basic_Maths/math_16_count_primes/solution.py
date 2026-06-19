# Time Complexity: O(N log(log N))
# Space Complexity: O(N)
# Explanation: Use the Sieve of Eratosthenes. Create a boolean array of size `n` initialized to true. Set indices 0 and 1 to false. Iterate from `p=2` to `sqrt(n)`. If `p` is prime, mark all its multiples starting from `p*p` as false. Count the remaining true values.

def countPrimes(n):
    if n <= 2: return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n, i):
                is_prime[j] = False
    return sum(is_prime)

