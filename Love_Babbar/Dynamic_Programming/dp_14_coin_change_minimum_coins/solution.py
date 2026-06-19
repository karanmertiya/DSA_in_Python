# Time Complexity: O(amount * N)
# Space Complexity: O(amount)
# Explanation: Create an array `dp` of size `amount + 1` initialized to `amount + 1` (acting as infinity). `dp[0] = 0`. For each amount from 1 to `amount`, for each coin, if `i - coin >= 0`, `dp[i] = min(dp[i], dp[i - coin] + 1)`.

def coinChange(coins: List[int], amount: int) -> int:
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] <= amount else -1

