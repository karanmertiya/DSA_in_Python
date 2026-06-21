# Time Complexity: O(M * N)
# Space Complexity: O(N)
# Explanation: Create a `dp` array of size `N + 1` initialized to 0. `dp[0] = 1`. For each coin, iterate through all amounts from `coin` to `N` and update `dp[j] += dp[j - coin]`.

def count(coins: List[int], N: int, sum: int) -> int:
    dp = [0] * (sum + 1)
    dp[0] = 1
    for coin in coins:
        for j in range(coin, sum + 1):
            dp[j] += dp[j - coin]
    return dp[sum]

