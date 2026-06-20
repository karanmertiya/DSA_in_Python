# Time Complexity: O(N log(log N))
# Space Complexity: O(N)
# Explanation: Use the Sieve of Eratosthenes. Initialize a boolean array of size `n` with `true`. Mark `0` and `1` as `false`. For each `i` from `2` to `sqrt(n)`, if `i` is prime, mark its multiples as `false` starting from `i*i`. Finally, count the number of `true`s.

def countPrimes(n: int) -> int:
    if n <= 2: return 0
    isPrime = [True] * n
    isPrime[0] = isPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n, i):
                isPrime[j] = False
    return sum(isPrime)

